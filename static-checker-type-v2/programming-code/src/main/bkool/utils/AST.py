from abc import ABC, abstractmethod, ABCMeta
from Visitor import Visitor


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)


class Program(AST):
    # decl:List[Decl],stmts:List[Stmt]
    def __init__(self, decl, stmts):
        self.decl = decl
        self.stmts = stmts

    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "]," + ','.join(str(s) for s in self.stmts) + ")"

    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)


class Decl(AST):
    __metaclass__ = ABCMeta
    pass


class FuncDecl(Decl):
    # name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
    def __init__(self, name, param, local, body):
        self.name = name
        self.param = param
        self.local = local
        self.body = body

    def __str__(self):
        return "FuncDecl(" + str(self.name) + ",[" + ','.join(str(i) for i in self.param) + "],[" + ','.join(str(i) for i in self.body) + "])"

    def accept(self, v, param):
        return v.visitFuncDecl(self, param)


class VarDecl(Decl):
    # name: str
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return "VarDecl(\"" + str(self.name) + "\")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)


class Type(AST):
    __metaclass__ = ABCMeta
    pass


class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)


class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)


class BoolType(Type):
    def __str__(self):
        return "BoolType"

    def accept(self, v, param):
        return v.visitBoolType(self, param)


class Stmt(AST):
    __metaclass__ = ABCMeta
    pass


class Expr(Stmt):
    __metaclass__ = ABCMeta
    pass


class LHS(Expr):
    __metaclass__ = ABCMeta
    pass


class Id(LHS):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(\"" + self.name + "\")"

    def accept(self, v, param):
        return v.visitId(self, param)


class Lit(Expr):
    __metaclass__ = ABCMeta
    pass


class IntLit(Lit):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLit(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLit(self, param)


class FloatLit(Lit):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "FloatLit(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitFloatLit(self, param)


class BoolLit(Lit):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BoolLit(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitBoolLit(self, param)


class BinOp(Expr):
    def __init__(self, op: str, e1: Expr, e2: Expr) -> None:
        self.op = op
        self.e1 = e1
        self.e2 = e2

    def __str__(self) -> str:
        return f'BinOp("{str(self.op)}",{str(self.e1)},{str(self.e2)})'

    def accept(self, v, param):
        return v.visitBinOp(self, param)


class UnOp(Expr):
    def __init__(self, op: str, e: Expr) -> None:
        self.op = op
        self.e = e

    def __str__(self) -> str:
        return f'UnOp("{str(self.op)}",{str(self.e)})'

    def accept(self, v, param):
        return v.visitUnOp(self, param)


class Assign(Stmt):
    # lhs:Id,rhs:Exp
    def __init__(self, lhs: Id, rhs: Expr) -> None:
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self) -> str:
        return f'Assign({str(self.lhs)},{str(self.rhs)})'

    def accept(self, v, param):
        return v.visitAssign(self, param)


class Block(Stmt):
    # decl:List[VarDecl],stmts:List[Stmt]
    def __init__(self, decl, stmts) -> None:
        self.decl = decl
        self.stmts = stmts

    def __str__(self) -> str:
        return "Block([" + ','.join(str(i) for i in self.decl) + "]," + ','.join(str(s) for s in self.stmts) + ")"

    def accept(self, v, param):
        return v.visitBlock(self, param)
