from functools import reduce
from os import pidfd_open
from typing import List
from Utils import *
from StaticCheck import *
from StaticError import *
from AST import *
import AST as ast
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
        return str(op) in ['>', '<', '>=', '<=', '==', '!=']

    @staticmethod
    def isOpForBooleanToBoolean(op):
        return str(op) in ['&&', '||']

    @staticmethod
    def isOpForStringToString(op):
        return str(op) == "::"

    @staticmethod
    def mergeNumberType(op, lType, rType):
        mTyp = None
        if type(lType) is IntegerType and type(rType) is IntegerType:
            if op == '+':
                mTyp = IntegerType(lType.val + rType.val)
            elif op == '-':
                mTyp = IntegerType(lType.val - rType.val)
            elif op == '*':
                mTyp = IntegerType(lType.val * rType.val)
            else:
                mTyp = IntegerType(lType.val % rType.val)
        else:
            mTyp = FloatType()
        return mTyp

    @staticmethod
    def retrieveType(originType, func=lambda x: x):
        if type(originType) is ast.IntegerType:
            return IntegerType()
        if type(originType) is ArrayType:
            arraySize, automicTyp = func(originType)
            originType.typ = MyUtils.retrieveType(
                originType.typ)  # ast.IntegerType
            return ArrayPointerType(originType.typ, arraySize, originType.dimensions)
        return originType

    @staticmethod
    def checkArrayType(code):
        if type(code) is list:
            return True
        return False


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
    def __init__(self, ctype, size=0, dimensions: List[int] = []):
        # cname: String
        self.eleType = ctype
        self.arraySize = size
        self.dimensions = dimensions

    def __str__(self):
        return "ArrayPointerType({0}, [{1}], {2})".format(str(self.arraySize), ", ".join([str(dimen) for dimen in self.dimensions]), str(self.eleType))

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


class IntegerType:
    def __init__(self, val: int = 0):
        self.val = val

    def __str__(self) -> str:
        return "IntegerType({0})".format(self.val)


class Dimensions():
    def __init__(self, dimensions: List[int] = [], curDimen=0, idxDimensions=[], idx=0):
        # [4, 3] - [0, 1]
        self.dimensions = dimensions
        self.curDimen = curDimen
        self.idxDimensions = idxDimensions
        self.idx = idx

    def __str__(self) -> str:
        return "Dimensions([{0}],{1})".format(", ".join([str(dimen) for dimen in self.dimensions]), str(self.curDimen))


class Access():
    def __init__(self, frame, sym, isLeft, elTypOfArray=None, dimen=Dimensions([])):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # elTypOfArray: Typ
        # dimen: Dimensions

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.elTypOfArray = elTypOfArray
        self.dimen = dimen


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
            for (name, typ, initCode) in self.globalVardecls:
                if type(typ) is ArrayPointerType:
                    self.emit.printout(self.emit.emitInitNewStaticArray(
                        self.className + "." + name, typ.arraySize, typ.eleType, initCode, frame))
                else:
                    if initCode != "":
                        self.emit.printout(
                            initCode + self.emit.emitPUTSTATIC(self.className + "." + name, typ, frame))

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
        typ = MyUtils.retrieveType(ast.typ, lambda x: self.visit(x, None))
        name = ast.name.name  # change this if error
        init = ast.init
        initCode = ""

        if init:
            if type(init) is ArrayLit:
                frame.push()  # need to push due to first initCode
                access = Access(frame, subctxt.sym, False,
                                elTypOfArray=typ.eleType, dimen=Dimensions(ast.typ.dimensions))
            else:
                access = Access(frame, subctxt.sym, False)
            initCode, initTyp = self.visit(init, access)
            initTyp = MyUtils.retrieveType(initTyp)
            if type(initTyp) is IntegerType and type(typ) is FloatType:
                initCode += self.emit.emitI2F(frame)

        if subctxt.isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(
                name, typ, False))
            self.globalVardecls.append((name, typ, initCode))
            print("============================ End VarDecl", ast)
            return Symbol(name, typ, CName(self.className))

        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame))

        if type(typ) is ArrayPointerType:
            self.emit.printout(self.emit.emitInitNewLocalArray(
                idx, typ.arraySize, typ.eleType, initCode, frame))
        else:
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

    def visitArrayType(self, ast: ArrayType, o: Access or None):
        dimensions = ast.dimensions
        typ = ast.typ
        return reduce(lambda x, y: x * y, dimensions[1:], dimensions[0]), typ

    def visitBlockStmt(self, ast: BlockStmt, o: SubBody):
        print("================================= BlockStmt")
        frame = o.frame
        sym = o.sym
        alreadyBlock = o.alreadyBlock
        hasReturnStmt = False
        if not alreadyBlock:  # for FuncDecl
            frame.enterScope(False)
            self.emit.printout(self.emit.emitLABEL(
                frame.getStartLabel(), frame))

        newSubBd = SubBody(frame, sym, alreadyBlock=True)
        for x in ast.body:
            if type(x) is VarDecl:
                newSubBd = self.visit(x, newSubBd)
            else:
                hasReturnStmt = self.visit(x, newSubBd) or hasReturnStmt

        if not alreadyBlock:
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            frame.exitScope()
        print("================================= End BlockStmt")
        return hasReturnStmt

    def visitBinExpr(self, ast: BinExpr, o: Access):
        leftCode, leftTyp = self.visit(ast.left, o)
        rightCode, rightTyp = self.visit(ast.right, o)
        op = ast.op
        frame = o.frame

        if MyUtils.isOpForNumber(op):
            mTyp = MyUtils.mergeNumberType(op, leftTyp, rightTyp)
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

    def visitArrayCell(self, ast: ArrayCell, o: Access):
        print("=========================== ArrayCell", ast)
        frame = o.frame
        sym = o.sym
        isLeft = o.isLeft
        cell = ast.cell
        nameCode, nameTyp = self.visit(
            ast.name, Access(frame, sym, isLeft))
        dimensions = nameTyp.dimensions
        idxDimensions = [self.visit(x, o)[1].val for x in cell]
        idx = 0
        # dimensions:    [4, 3, 4]
        # idxDimensions: [1, 2, 5] -> idx = (1 * 3 * 4) + (2 * 3) + 5
        for i, idxDimen in enumerate(idxDimensions):
            idx += reduce(lambda x, y: x * y,
                          dimensions[i+1:], idxDimen)

        print("=========================== End ArrayCell")
        if isLeft:
            return [nameCode + self.emit.emitPUSHICONST(idx, frame), self.emit.emitASTORE(nameTyp.eleType, frame)], nameTyp.eleType
        return nameCode + self.emit.emitPUSHICONST(idx, frame) + self.emit.emitALOAD(nameTyp.eleType, frame), nameTyp.eleType

    def visitAssignStmt(self, ast: AssignStmt, o: SubBody):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym
        rhsCode, rhsTyp = self.visit(ast.rhs, Access(frame, sym, False))
        lhsCode, lhsTyp = self.visit(ast.lhs, Access(frame, sym, True))
        if type(rhsTyp) is IntegerType and type(lhsTyp) is FloatType:
            rhsCode += self.emit.emitI2F(frame)
        if MyUtils.checkArrayType(lhsCode):
            self.emit.printout(lhsCode[0] + rhsCode + lhsCode[1])
        else:
            self.emit.printout(rhsCode + lhsCode)

    def visitIfStmt(self, ast: IfStmt, o: SubBody):
        frame = o.frame
        sym = o.sym
        condCode, _ = self.visit(
            ast.cond, Access(frame, sym, False))
        self.emit.printout(condCode)

        labelF = frame.getNewLabel()  # eval is false
        labelE = frame.getNewLabel()  # label end

        self.emit.printout(self.emit.emitIFFALSE(labelF, frame))

        hasReturnStmt = self.visit(ast.tstmt, o) is True
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelE, frame))

        self.emit.printout(self.emit.emitLABEL(labelF, frame))
        if ast.fstmt:
            print(self.visit(ast.fstmt, o))

        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        return hasReturnStmt

    def visitForStmt(self, ast, o):
        pass

    def visitWhileStmt(self, ast, o):
        frame = o.frame
        sym = o.sym
        labelW = frame.getNewLabel()  # label while
        labelE = frame.getNewLabel()  # label end
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelW, frame))
        exp_j, exp_typ = self.visit(ast.expr, Access(frame, sym, False))
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

    def visitReturnStmt(self, ast: ReturnStmt, o: SubBody):
        print("========================= ReturnStmt", ast)
        print("========================= End ReturnStmt")
        return True

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
                x, Access(frame, o.sym, False))
            paramsCode += exprCode
        self.emit.printout(paramsCode + self.emit.emitINVOKESTATIC(
            cName + "/" + sym.name, cTyp, frame))
        print("========================= End CallStmt")

    def visitIntegerLit(self, ast: IntegerLit, o: Access):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType(ast.val)

    def visitFloatLit(self, ast: FloatLit, o: Access):
        return self.emit.emitPUSHFCONST(str(ast.val), o.frame), FloatType()

    def visitBooleanLit(self, ast: BooleanLit, o: Access):
        return self.emit.emitPUSHICONST(str(ast.val).lower(), o.frame), BooleanType()

    def visitStringLit(self, ast: StringLit, o: Access):
        return self.emit.emitPUSHCONST(ast.val, StringType(), o.frame), StringType()

    def visitArrayLit(self, ast: ArrayLit, o: Access):
        frame = o.frame
        dimen = o.dimen
        explist = ast.explist
        expCode = ""
        expTyp = o.elTypOfArray
        for i, x in enumerate(explist):
            # change multidimensions into single dimension
            # dimensions:    [4, 3, 4]
            # idxDimensions: [1, 2, 5] -> idx = (1 * 3 * 4) + (2 * 3) + 5
            dimen.idxDimensions.append(i)
            if type(x) is ArrayLit:
                dimen.curDimen += 1
            val = reduce(
                lambda x, y: x * y, dimen.dimensions[dimen.curDimen:], dimen.idxDimensions[dimen.curDimen - 1])
            if len(dimen.dimensions) == len(dimen.idxDimensions):
                val = dimen.idxDimensions[dimen.curDimen]
            dimen.idx += val

            eC, eT = self.visit(x, o)

            if type(x) is ArrayLit:
                dimen.curDimen -= 1
            if type(x) is not ArrayLit:
                if type(eT) is IntegerType and type(expTyp) is FloatType:
                    eC += self.emit.emitI2F(frame)
                expCode += self.emit.emitDUP(
                    frame) + self.emit.emitPUSHCONST(str(dimen.idx), expTyp, frame) + eC + self.emit.emitASTORE(expTyp, frame)
            else:
                expCode += eC
            dimen.idx -= val
            dimen.idxDimensions.pop()
        return expCode, expTyp

    def visitId(self, ast: Id, o: Access):
        frame = o.frame
        for s in o.sym:
            if ast.name == s.name:
                isArrayType = type(s.mtype) is ArrayPointerType
                if type(s.value) is CName:
                    if o.isLeft == True and not isArrayType:
                        return self.emit.emitPUTSTATIC(s.value.value + '.' + ast.name, s.mtype, frame), s.mtype
                    return self.emit.emitGETSTATIC(s.value.value + '.' + ast.name, s.mtype, frame), s.mtype
                if o.isLeft == True and not isArrayType:
                    return self.emit.emitWRITEVAR(ast.name, s.mtype, s.value.value, frame), s.mtype
                return self.emit.emitREADVAR(ast.name, s.mtype, s.value.value, frame), s.mtype
