from abc import *
from typing import List


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)


class Expr(AST):
    __metaclass__ = ABCMeta
    pass


class Id(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)


class Type(ABC):
    pass


class IntType(Type):
    def __str__(self):
        return self.__class__.__name__


class FloatType(Type):
    def __str__(self):
        return self.__class__.__name__


class VarDecl:  # variable:Id; vartype: Type
    def __init__(self, variable: Id, vartype: Type):
        self.variable = variable
        self.vartype = vartype

    def __str__(self):
        return "VarDecl({},{})".format(self.variable, str(self.vartype))

    def accept(self, v, param):
        return v.visitVarDecl(self, param)


class Program:  # decl:list(VarDecl)
    def __init__(self, decl: List[VarDecl]):
        self.decl = decl

    def __str__(self):
        return "Program([{}])".format(",".join([str(decl) for decl in self.decl]))
