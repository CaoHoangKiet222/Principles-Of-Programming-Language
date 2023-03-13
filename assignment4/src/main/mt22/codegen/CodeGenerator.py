from Utils import *
from StaticCheck import *
from StaticError import *
from AST import *
from Visitor import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


class MyUtils:
    @staticmethod
    def isOpForNumber(op):
        return MyUtils.isOpForNumberToNumber(op) or MyUtils.isOpForNumberToBoolean(op)

    @staticmethod
    def isOpForNumberToNumber(op):
        return str(op) in ['+', '-', '*', '/', '%']

    @staticmethod
    def isOpForNumberToBoolean(op):
        return str(op) in ['>', '<', '>=', '<=']

    @staticmethod
    def isOpForBooleanToBoolean(op):
        return str(op) in ['&&', '||']

    @staticmethod
    def isOpForStringToString(op):
        return str(op) == "::"

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntegerType()

    @staticmethod
    def retrieveType(originType):
        if type(originType) is ArrayType:
            return ArrayPointerType(originType.eleType)
        return originType


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
    def __init__(self, frame, sym, alreadyBlock=False, isGlobal=False):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.alreadyBlock = alreadyBlock
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
        self.globalVardecls = []

    def visitProgram(self, ast: Program, c):
        print("============================= Program", ast)
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))

        globalEnv = self.env
        glFrame = Frame("<clinit>", VoidType)
        # global declarations
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                pass
            else:
                newSym = self.visit(decl, SubBody(
                    glFrame, globalEnv, isGlobal=True))
                globalEnv.append(newSym)

        e = SubBody(None, globalEnv)
        [self.visit(decl, e) for decl in ast.decls if type(decl) is FuncDecl]

        # # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), None, list(), None,
                       BlockStmt(list())), c, Frame("<init>", VoidType))

        self.genMETHOD(FuncDecl(Id("<clinit>"), None, list(),
                       None, BlockStmt(list())), c, glFrame)

        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, decl: FuncDecl, o, frame: Frame):
        # decl: FuncDecl
        # o: Any
        # frame: Frame
        glenv = o
        methodName = decl.name.name  # change this if error
        body = decl.body

        isInit = decl.return_type is None and methodName == "<init>"
        isStaticInit = decl.return_type is None and methodName == "<clinit>"
        isMain = methodName == "main" and len(
            decl.params) == 0 and type(decl.return_type) is VoidType
        returnType = VoidType() if isInit or isStaticInit else decl.return_type
        isProc = type(returnType) is VoidType
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        if not isStaticInit:
            frame.enterScope(isProc)
        else:
            frame.enterScope(False)

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
        if isStaticInit:
            [self.emit.printout(initCode + self.emit.emitPUTSTATIC(self.className + "." + name, typ, frame))
             for (name, typ, initCode) in self.globalVardecls]

        self.visit(body, SubBody(frame, glenv, alreadyBlock=True))

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
        init = ast.init
        initCode = None

        if init:
            initCode, initTyp = self.visit(
                init, Access(frame, subctxt.sym, False, False))
            if type(initTyp) is IntegerType and type(typ) is FloatType:
                initCode += self.emit.emitI2F(frame)

        if subctxt.isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(
                name, typ, False))
            if initCode:
                self.globalVardecls.append((name, typ, initCode))
            print("============================ End VarDecl", ast)
            return Symbol(name, typ, CName(self.className))

        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame))

        if initCode:
            self.emit.printout(
                initCode + self.emit.emitWRITEVAR(name, typ, idx, frame))
        print("============================ End VarDecl", ast)
        return SubBody(frame, [Symbol(name, typ, Index(idx))] + subctxt.sym)

    def visitParamDecl(self, ast: ParamDecl, o: Access):
        print("============================ ParamDecl", ast)
        print("============================ End ParamDecl")

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
        sym = o.sym
        alreadyBlock = o.alreadyBlock
        if not alreadyBlock:
            frame.enterScope(False)
            self.emit.printout(self.emit.emitLABEL(
                frame.getStartLabel(), frame))

        newSubBd = SubBody(frame, sym, alreadyBlock=True)
        for x in ast.body:
            if type(x) is VarDecl:
                newSubBd = self.visit(x, newSubBd)
            else:
                self.visit(x, newSubBd)

        if not alreadyBlock:
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            frame.exitScope()
        print("================================= End BlockStmt")

    def visitBinExpr(self, ast: BinExpr, o: Access):
        leftCode, leftTyp = self.visit(ast.left, o)
        rightCode, rightTyp = self.visit(ast.right, o)
        op = ast.op
        frame = o.frame

        if MyUtils.isOpForNumber(op):
            mTyp = MyUtils.mergeNumberType(leftTyp, rightTyp)
            if op == '/':
                mTyp = FloatType()
            if type(leftTyp) is IntegerType and type(mTyp) != type(leftTyp):
                leftCode = leftCode + self.emit.emitI2F(frame)
            if type(rightTyp) is IntegerType and type(mTyp) != type(rightTyp):
                rightCode = rightCode + self.emit.emitI2F(frame)
            if MyUtils.isOpForNumberToNumber(op):
                if op in ['+', '-']:
                    return leftCode + rightCode + self.emit.emitADDOP(op, mTyp, frame), mTyp
                if op in ['*', '/']:
                    return leftCode + rightCode + self.emit.emitMULOP(op, mTyp, frame), mTyp
                if op == '%':
                    return leftCode + rightCode + self.emit.emitMOD(frame), mTyp
            if MyUtils.isOpForNumberToBoolean(op):
                return leftCode + rightCode + self.emit.emitREOP(op, mTyp, frame), BooleanType()
        if MyUtils.isOpForStringToString(op):
            leftVal = leftCode.replace("\tldc ", "").replace(
                "\"", "").removesuffix('\n')
            rightVal = rightCode.replace("\tldc ", "").replace(
                "\"", "").removesuffix('\n')
            return self.emit.emitPUSHCONST(str(leftVal + rightVal), StringType(), frame), StringType()
        if MyUtils.isOpForBooleanToBoolean(op):
            mTyp = BooleanType()
            return leftCode + rightCode + (self.emit.emitANDOP(frame) if op == '&&' else self.emit.emitOROP(frame)), mTyp

    def visitUnExpr(self, ast: UnExpr, o: Access):
        frame = o.frame
        op = ast.op
        valCode, valTyp = self.visit(ast.val, o)
        if op == '-':
            return valCode + self.emit.emitNEGOP(valTyp, frame), valTyp
        if op == '!':
            return valCode + self.emit.emitNOT(valTyp, frame), valTyp

    def visitArrayCell(self, ast, o):
        pass

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
        print("========================= CallStmt", ast)
        frame = o.frame
        # change this if error
        sym = self.lookup(ast.name.name, o.sym, lambda x: x.name)
        cName = sym.value.value
        cTyp = sym.mtype
        paramsCode = ""
        for x in ast.args:
            exprCode, exprTyp = self.visit(
                x, Access(frame, o.sym, False, True))
            paramsCode += exprCode
        self.emit.printout(paramsCode + self.emit.emitINVOKESTATIC(
            cName + "/" + sym.name, cTyp, frame))
        print("========================= End CallStmt")

    def visitIntegerLit(self, ast: IntegerLit, o: Access):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()

    def visitFloatLit(self, ast: FloatLit, o: Access):
        return self.emit.emitPUSHFCONST(str(ast.val), o.frame), FloatType()

    def visitBooleanLit(self, ast: BooleanLit, o: Access):
        return self.emit.emitPUSHICONST(str(ast.val).lower(), o.frame), BooleanType()

    def visitStringLit(self, ast: StringLit, o: Access):
        return self.emit.emitPUSHCONST(ast.val, StringType(), o.frame), StringType()

    def visitArrayLit(self, ast, o):
        pass

    def visitId(self, ast: Id, o: Access):
        print("====================== Id", ast)
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
