from abc import *


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)


class Expr(AST):
    __metaclass__ = ABCMeta
    pass


class Type(AST):
    pass


class CompoundType(Type):
    pass


class UnionType(CompoundType):
    # firstType:Type,secondType:PrimType
    def __init__(self, firstType, secondType):
        self.firstType = firstType
        self.secondType = secondType

    def __str__(self):
        return "UnionType(" + str(self.firstType) + "," + str(self.secondType) + ")"

    def accept(self, v, param):
        return v.visitUnionType(self, param)


class ArrayType(CompoundType):
    # indexType:Type,eleType:primType
    def __init__(self, indexType, eleType):
        self.indexType = indexType
        self.eleType = eleType

    def __str__(self):
        return "ArrayType(" + str(self.indexType) + "," + str(self.eleType) + ")"

    def accept(self, v, param):
        return v.visitArrayType(self, param)


class PrimType(Type):
    pass


class IntType:
    def __str__(self) -> str:
        return self.__class__.__name__


class FloatType:
    def __str__(self) -> str:
        return self.__class__.__name__


class RangeType(PrimType):
    # lowbound:int; highbound:int
    def __init__(self, lowbound, highbound):
        self.lowbound = lowbound
        self.highbound = highbound

    def __str__(self):
        return "RangeType(" + str(self.lowbound) + "," + str(self.highbound) + ")"

    def accept(self, v, param):
        return v.visitRangeType(self, param)


class Id(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)
