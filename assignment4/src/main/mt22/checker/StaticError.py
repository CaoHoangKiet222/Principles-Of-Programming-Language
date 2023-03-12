from abc import ABC
from dataclasses import dataclass
from AST import *


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


@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str  # name of identifier

    def __str__(self):
        return "Redeclared " + str(self.k) + ": " + self.n


@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str  # name of identifier

    def __str__(self):
        return "Undeclared " + str(self.k) + ": " + self.n


@dataclass
class Invalid(StaticError):
    k: Kind
    n: str  # name of variable/parameter

    def __str__(self):
        return "Invalid " + str(self.k) + ": " + self.n


@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Expr

    def __str__(self):
        return "Type Mismatch In Expression: " + str(self.exp)


@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: Stmt

    def __str__(self):
        return "Type Mismatch In Statement: " + str(self.stmt)


@dataclass
class MustInLoop(StaticError):
    stmt: Stmt

    def __str__(self):
        return str(self.stmt) + " Not In Loop"


@dataclass
class IllegalArrayLiteral(StaticError):
    arr: ArrayLit

    def __str__(self):
        return "Illegal Array Literal: " + str(self.arr)


@dataclass
class InvalidStatementInFunction(StaticError):
    n: str  # name of function

    def __str__(self):
        return "Invalid Statement In Function: " + str(self.n)


@dataclass
class NoEntryPoint(StaticError):
    def __str__(self) -> str:
        return "No Entry Point"
