# update: 16/07/2018
from abc import ABC


class Kind(ABC):
    pass


class Function(Kind):
    def __str__(self):
        return "Function"


class Parameter(Kind):
    def __str__(self):
        return "Parameter"


class Variable(Kind):
    def __str__(self):
        return "Variable"


class Identifier(Kind):
    def __str__(self):
        return "Identifier"


class StaticError(Exception):
    pass


class UndeclaredIdentifier(StaticError):
    """k: Kind
       n: string: name of identifier """

    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "Undeclared Identifier: " + self.n


class Redeclared(StaticError):
    """k: Kind
       n: string: name of identifier """

    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "Redeclared: " + str(self.n)


class RedeclaredConstant(StaticError):
    """k: Kind
       n: string: name of identifier """

    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "Redeclared Constant: " + str(self.n)


class RedeclaredFunction(StaticError):
    """k: Kind
       n: string: name of identifier """

    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "Redeclared Function: " + str(self.n)


class TypeMismatchInExpression(StaticError):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return "Type Mismatch In Expression: " + str(self.expr)


class TypeMismatchInStatement(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "Type Mismatch In Statement: " + str(self.stmt)


class TypeCannotBeInferred(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "Type Cannot Be Inferred: " + str(self.stmt)
