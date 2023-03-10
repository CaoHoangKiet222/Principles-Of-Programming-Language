from Utils import *
from StaticCheck import *
from StaticError import *
from AST import *
from Visitor import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("putFloat", MType(
                    [FloatType()], VoidType()), CName(self.libName))

                ]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class StringType(Type):

    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None


class ArrayPointerType(Type):
    def __init__(self, ctype):
        # cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        # value: String

        self.value = value


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "BKOOLClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        # ast: Program
        # c: Any

        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            # e = self.visit(x, e)
            print("Program", self.visit(x, e))
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(
            list(), list())), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        # consdecl: FuncDecl
        # o: Any
        # frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(
            consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.decl))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    # Quiz 6
    def visitVarDecl(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        typ = ast.typ
        name = ast.name.name
        if frame is None:  # a global declaration
            self.emit.printout(self.emit.emitATTRIBUTE(name, typ, False))
            return Symbol(name, typ, CName(self.className))
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame))
        return Symbol(name, typ, Index(idx))

    def visitFuncDecl(self, ast, o):
        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    def visitBlock(self, ast, o):
        frame = o.frame
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        list(map(lambda x: self.visit(x, SubBody(frame, o.sym)), ast.decl))
        list(map(lambda x: self.visit(x, SubBody(frame, o.sym)), ast.stmt))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    def visitCallExpr(self, ast, o):
        frame = o.frame
        nenv = o.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value

        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    # Quiz 3
    def visitBinExpr(self, ast, o):
        frame = o.frame

        e1_j, typ_e1 = self.visit(ast.e1, o)
        self.emit.printout(e1_j)
        e2_j, typ_e2 = self.visit(ast.e2, o)
        self.emit.printout(e2_j)
        if ast.op in ['+', '-']:
            return self.emit.emitADDOP(ast.op, IntType(), frame), IntType()
        if ast.op in ['*', '/']:
            return self.emit.emitMULOP(ast.op, IntType(), frame), IntType()
        if ast.op in ['+.', '-.']:
            return self.emit.emitADDOP(ast.op[0], FloatType(), frame), FloatType()
        if ast.op in ['*.', '/.']:
            return self.emit.emitMULOP(ast.op[0], FloatType(), frame), FloatType()

    # Quiz 5
    # def visitBinExpr(self, ctx, o):
    #     e1str, e1type = ctx.e1.accept(self, o)
    #     e2str, e2type = ctx.e2.accept(self, o)

    #     if ctx.op in ['+', '-']:
    #         if type(e1type) is FloatType and type(e2type) is IntType:
    #             return e1str + e2str + self.emit.emitI2F(o.frame) + self.emit.emitADDOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is IntType and type(e2type) is FloatType:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitADDOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is FloatType and type(e2type) is FloatType:
    #             return e1str + e2str + self.emit.emitADDOP(ctx.op, FloatType(), o.frame), FloatType()
    #         else:
    #             return e1str + e2str + self.emit.emitADDOP(ctx.op, IntType(), o.frame), IntType()

    #     if ctx.op == '*':
    #         if type(e1type) is FloatType and type(e2type) is IntType:
    #             return e1str + e2str + self.emit.emitI2F(o.frame) + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is IntType and type(e2type) is FloatType:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is FloatType and type(e2type) is FloatType:
    #             return e1str + e2str + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()
    #         else:
    #             return e1str + e2str + self.emit.emitMULOP(ctx.op, IntType(), o.frame), IntType()

    #     if ctx.op == '/':
    #         if type(e1type) is FloatType and type(e2type) is IntType:
    #             return e1str + e2str + self.emit.emitI2F(o.frame) + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is IntType and type(e2type) is FloatType:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is FloatType and type(e2type) is FloatType:
    #             return e1str + e2str + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()
    #         else:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitI2F(o.frame) + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()
    #     else:
    #         if type(e1type) is FloatType and type(e2type) is IntType:
    #             return e1str + e2str + self.emit.emitI2F(o.frame) + self.emit.emitREOP(ctx.op, FloatType(), o.frame), BoolType()

    #         if type(e1type) is IntType and type(e2type) is FloatType:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitREOP(ctx.op, FloatType(), o.frame), BoolType()

    #         if type(e1type) is FloatType and type(e2type) is FloatType:
    #             return e1str + e2str + self.emit.emitREOP(ctx.op, FloatType(), o.frame), BoolType()
    #         else:
    #             return e1str + e2str + self.emit.emitREOP(ctx.op, IntType(), o.frame), BoolType()

    def visitAssign(self, ast, o):
        frame = o.frame
        sym = o.sym
        rhs_j, rhs_typ = self.visit(ast.rhs, Access(frame, sym, False, False))
        lsh_j, lsh_typ = self.visit(ast.lhs, Access(frame, sym, True, False))
        self.emit.printout(rhs_j + lsh_j)

    def visitIf(self, ast, o):
        frame = o.frame
        sym = o.sym
        exp_j, exp_typ = self.visit(
            ast.expr, Access(frame, sym, False, False))
        self.emit.printout(exp_j)

        labelF = frame.getNewLabel()  # eval is false
        labelE = frame.getNewLabel()  # label end

        self.emit.printout(self.emit.emitIFFALSE(labelF, frame))

        self.visit(ast.tstmt, o)
        self.emit.printout(self.emit.emitGOTO(labelE, frame))

        self.emit.printout(self.emit.emitLABEL(labelF, frame))
        if ast.estmt:
            self.visit(ast.estmt, o)

        self.emit.printout(self.emit.emitLABEL(labelE, frame))

    def visitWhile(self, ast, o):
        frame = o.frame
        sym = o.sym
        labelW = frame.getNewLabel()  # label while
        labelE = frame.getNewLabel()  # label end
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelW, frame))
        exp_j, exp_typ = self.visit(ast.expr, Access(frame, sym, False, False))
        self.emit.printout(exp_j + self.emit.emitIFFALSE(labelE, frame))
        self.visit(ast.stmt, o)
        self.emit.printout(self.emit.emitLABEL(
            frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitGOTO(
            labelW, frame) + self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(
            frame.getBreakLabel(), frame))
        frame.exitLoop()

    # Quiz 1
    def visitIntLiteral(self, ast, o):
        frame = o.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    # Quiz 2
    def visitFloatLiteral(self, ast, o):
        frame = o.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBoolLiteral(self, ast, o):
        frame = o.frame
        return self.emit.emitPUSHICONST(ast.value, frame), BoolType()

    # Quiz 4
    def visitId(self, ast, o):
        frame = o.frame
        for s in o.sym:
            if ast.name == s.name:
                if type(s.value) is CName:
                    if o.isLeft == True:
                        return self.emit.emitPUTSTATIC(s.value.value + '.' + ast.name, s.mtype, frame), s.mtype
                    return self.emit.emitGETSTATIC(s.value.value + '.' + ast.name, s.mtype, frame), s.mtype
                if o.isLeft == True:
                    return self.emit.emitWRITEVAR(ast.name, s.mtype, s.value.value, frame), s.mtype
                return self.emit.emitREADVAR(ast.name, s.mtype, s.value.value, frame), s.mtype
