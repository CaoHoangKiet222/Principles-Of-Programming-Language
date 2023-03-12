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
        return [
            Symbol("readInteger", MType([], IntegerType()), CName(self.libName)),
            Symbol("printInteger", MType(
                [IntegerType()], VoidType()), CName(self.libName)),
            Symbol("readFloat", MType([], FloatType()), CName(self.libName)),
            Symbol("writeFloat", MType(
                [FloatType()], VoidType()), CName(self.libName)),
            Symbol("readBoolean", MType([], BooleanType()), CName(self.libName)),
            Symbol("printBoolean", MType(
                [BooleanType()], VoidType()), CName(self.libName)),
            Symbol("readString", MType([], StringType()), CName(self.libName)),
            Symbol("printString", MType(
                [StringType()], VoidType()), CName(self.libName)),
            Symbol("super", MType([List[Expr]],
                   VoidType()), CName(self.libName)),
            Symbol("preventDefault", MType(
                [], VoidType()), CName(self.libName)),
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
    def __init__(self, frame, sym, isGlobal=False):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal


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
        # value: int
        self.value = value

    def __str__(self) -> str:
        return "Index({})".format(str(self.value))


class CName(Val):
    def __init__(self, value):
        # value: str
        self.value = value

    def __str__(self) -> str:
        return "CName({})".format(str(self.value))


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast: Program, c):
        print("============================= Program", ast)

        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))

        globalEnv = self.env
        # global declarations
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                pass
            else:
                newSym = self.visit(decl, SubBody(
                    None, self.env, isGlobal=True))
                globalEnv.append(newSym)

        e = SubBody(None, globalEnv)
        [self.visit(decl, e) for decl in ast.decls if type(decl) is FuncDecl]

        # # generate default constructor
        # change this if error
        self.genMETHOD(FuncDecl(Id("<init>"), VoidType(), list(), None,
                       BlockStmt(list())), c, Frame("<init>", VoidType))

        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl: FuncDecl, o, frame: Frame):
        # consdecl: FuncDecl
        # o: Any
        # frame: Frame
        glenv = o
        name = consdecl.name.name  # change this if error
        return_type = consdecl.return_type
        params = consdecl.params
        body = consdecl.body
        isProc = type(return_type) is VoidType

        isInit = return_type is None
        # change this if error
        isMain = name == "main" and len(
            params) == 0 and type(return_type) is VoidType
        returnType = VoidType() if isInit else return_type
        methodName = "<init>" if isInit else name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(isProc)

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        self.visit(body, SubBody(frame, glenv))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isProc:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitVarDecl(self, ast: VarDecl, o: SubBody):
        print("============================ VarDecl", ast)
        subctxt = o
        frame = subctxt.frame
        typ = ast.typ
        name = ast.name.name  # change this if error
        if subctxt.isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(name, typ, False))
            print("============================ End VarDecl", ast)
            return Symbol(name, typ, CName(self.className))
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame))
        print("============================ End VarDecl", ast)
        return Symbol(name, typ, Index(idx))

    def visitParamDecl(self, ast, o):
        pass

    def visitFuncDecl(self, ast: FuncDecl, o: SubBody):
        print("============================ FuncDecl", ast)
        subctxt = o
        name = ast.name.name
        return_type = ast.return_type
        frame = Frame(name, return_type)
        self.genMETHOD(ast, subctxt.sym, frame)
        print("============================ End FuncDecl")
        return SubBody(None, [Symbol(name, MType(list(), return_type), CName(self.className))] + subctxt.sym)

    def visitIntegerType(self, ast, o):
        pass

    def visitFloatType(self, ast, o):
        pass

    def visitBooleanType(self, ast, o):
        pass

    def visitStringType(self, ast, o):
        pass

    def visitVoidType(self, ast, o):
        pass

    def visitAutoType(self, ast, o):
        pass

    def visitArrayType(self, ast, o):
        pass

    def visitBlockStmt(self, ast: BlockStmt, o: SubBody):
        print("================================= BlockStmt")
        frame = o.frame
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        list(map(lambda x: self.visit(x, SubBody(frame, o.sym)), ast.body))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        print("================================= End BlockStmt")

    def visitFuncCall(self, ast, o):
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

    def visitUnExpr(self, ast, param):
        pass

    def visitArrayCell(self, ast, param):
        pass

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

    def visitAssignStmt(self, ast, o):
        frame = o.frame
        sym = o.sym
        rhs_j, rhs_typ = self.visit(ast.rhs, Access(frame, sym, False, False))
        lsh_j, lsh_typ = self.visit(ast.lhs, Access(frame, sym, True, False))
        self.emit.printout(rhs_j + lsh_j)

    def visitIfStmt(self, ast, o):
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

    def visitForStmt(self, ast, o):
        pass

    def visitWhileStmt(self, ast, o):
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

    def visitDoWhileStmt(self, ast, o):
        pass

    def visitContinueStmt(self, ast, o):
        pass

    def visitBreakStmt(self, ast, o):
        pass

    def visitReturnStmt(self, ast, o):
        pass

    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        pass

    def visitIntegerLit(self, ast, o):
        frame = o.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLit(self, ast, o):
        frame = o.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLit(self, ast, o):
        frame = o.frame
        return self.emit.emitPUSHICONST(ast.value, frame), BoolType()

    def visitStringLit(self, ast, o):
        pass

    def visitArrayLit(self, ast, o):
        pass

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
