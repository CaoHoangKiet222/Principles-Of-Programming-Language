"""
 * @author nhphung
 * Student's name: Cao Hoang Kiet
 * Student's ID: 2053165
"""

from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import reduce


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


@dataclass
class ArrayTyp(Type):
    num_of_el: int
    el_typ: Type

    def __str__(self) -> str:
        return "ArrayTyp({},{})".format(str(self.num_of_el), str(self.el_typ))


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class CheckUtils:
    @staticmethod
    def dimensionsMatch(dimensions1: List[int], dimensions2: List[int]):
        print(dimensions1, dimensions2)
        if dimensions2[0] == 0:
            return True
        if len(dimensions1) != len(dimensions2):
            return False
        for idx, i in enumerate(dimensions1):
            if i < dimensions2[idx]:
                return False
        return True


class TypUtils:
    @staticmethod
    def retriveType(typ: Type):
        # typ: ArrayTyp(2,ArrayTyp(4,IntegerType)) -> IntegerType
        return TypUtils.retriveType(typ.el_typ) if ExpUtils.isArrayLit(typ) else typ

    @staticmethod
    def retriveDimensions(typ: Type):
        # typ: ArrayTyp(2,ArrayTyp(4,IntegerType)) -> [2, 4]
        return [typ.num_of_el, *TypUtils.retriveDimensions(typ.el_typ)] if ExpUtils.isArrayLit(typ) else []

    @staticmethod
    def impConversion(typ: Type, init_typ: Type, callback):
        if type(typ) is IntegerType:
            if type(init_typ) is FloatType:
                callback()
                return
        elif type(typ) is FloatType:
            if type(init_typ) is IntegerType:
                return FloatType()
        return init_typ


class ExpUtils:
    @staticmethod
    def isNotIntFloatLit(expr):
        return type(expr) not in [IntegerType, FloatType]

    @staticmethod
    def isNotIntBoolLit(expr):
        return type(expr) not in [IntegerType, BooleanType]

    @staticmethod
    def isNotIntLit(expr):
        return type(expr) is not IntegerType

    @staticmethod
    def isNotBoolLit(expr):
        return type(expr) is not BooleanType

    @staticmethod
    def isNotStringLit(expr):
        return type(expr) is not StringType

    @staticmethod
    def isArrayLit(expr):
        return type(expr) is ArrayTyp

    @staticmethod
    def isTheSameType(expr1, expr2):
        return type(expr1) is type(expr2)


def infer(id: Id, type, o):
    for env in o:
        if id.name in env:
            if env[id.name] is None:
                env[id.name] = type
                return type
            else:
                return env[id.name]
    return None


class StaticChecker(BaseVisitor):
    global_envi = [
        Symbol("readInteger", MType([], IntegerType())),
        Symbol("printInteger", MType([IntegerType()], VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("writeFloat", MType([FloatType()], VoidType())),
        Symbol("readBoolean", MType([], BooleanType())),
        Symbol("printBoolean", MType([BooleanType()], VoidType())),
        Symbol("readString", MType([], StringType())),
        Symbol("printString", MType([StringType()], VoidType())),
        Symbol("super", MType([[Expr()]], VoidType())),
        Symbol("preventDefault", MType([], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast
        self.global_env = [{}]
        self.illegal_array_lit = False

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)

    def setIlligalArrayLit(self, value):
        self.illegal_array_lit = value

    def __raise(self, ex):
        raise ex

    def visitProgram(self, ast: Program, c):
        # decls: List[Decl]
        # c has structure
        # [
        #   {
        #      variable_name: {"kind": Variable/Parameter, "typ": Type},
        #      method_name: {"kind": Function, "return_typ": Type, "params": [Type]},
        #   }
        # ]
        c = self.global_env

        for decl in ast.decls:
            self.visit(decl, c)
        return ""

    def visitVarDecl(self, ast: VarDecl, c):
        name = ast.name.name  # change this if error
        typ = self.visit(ast.typ, c)
        init = ast.init
        if name in c[0]:
            raise Redeclared(Variable(), name)

        if init is not None:
            if type(typ) is ArrayType:
                init_typ = self.visit(init, (c, typ))
                if self.illegal_array_lit:
                    raise TypeMismatchInStatement(ast)
                print(init_typ)
                # Check dimensions initialization match with its array_type_dimensions
                if not CheckUtils.dimensionsMatch(typ.dimensions, TypUtils.retriveDimensions(init_typ)):
                    raise TypeMismatchInStatement(ast)

            else:
                init_typ = self.visit(init, (c))
                # Check error when implicit conversion --> Case: float / integer
                init_typ = TypUtils.impConversion(
                    typ, init_typ, lambda: self.__raise(
                        TypeMismatchInStatement(ast)))
                # Need to infer type when initialization
                if type(typ) is AutoType:
                    typ = init_typ
                # Check type element in automic_lit is similar with type of its type
                if not ExpUtils.isTheSameType(typ, init_typ):
                    raise TypeMismatchInStatement(ast)

        c[0][name] = {"kind": Variable(), "typ": typ}

    def visitParamDecl(self, ast, c):
        pass

    def visitFuncDecl(self, ast, c):
        pass

    def visitIntegerType(self, ast: IntegerType, c):
        return IntegerType()

    def visitFloatType(self, ast: FloatType, c):
        return FloatType()

    def visitBooleanType(self, ast: BooleanType, c):
        return BooleanType()

    def visitStringType(self, ast: StringType, c):
        return StringType()

    def visitVoidType(self, ast: VoidType, c):
        return VoidType()

    def visitAutoType(self, ast: AutoType, c):
        return AutoType()

    def visitArrayType(self, ast: ArrayType, c):
        return ast

    def visitBinExpr(self, ast: BinExpr, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        if ast.op in ['+', '-', '*', '/']:
            if ExpUtils.isNotIntFloatLit(left) or ExpUtils.isNotIntFloatLit(right):
                raise TypeMismatchInExpression(ast)
            if type(left) is FloatType or type(right) is FloatType:
                return FloatType()
            return IntegerType()
        if ast.op == '%':
            if ExpUtils.isNotIntLit(left) or ExpUtils.isNotIntLit(right):
                raise TypeMismatchInExpression(ast)
            return IntegerType()
        if ast.op in ['&&', '||']:
            if ExpUtils.isNotBoolLit(left) or ExpUtils.isNotBoolLit(right):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if ast.op in ['==', '!=']:
            if ExpUtils.isNotIntBoolLit(left) or ExpUtils.isNotIntBoolLit(right):
                raise TypeMismatchInExpression(ast)
            # Not update assignment yet
            if type(left) is not type(right):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if ast.op in ['>', '<', '>=', '<=']:
            if ExpUtils.isNotIntFloatLit(left) or ExpUtils.isNotIntFloatLit(right):
                raise TypeMismatchInExpression(ast)
            # Not update assignment yet
            if type(left) is not type(right):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if ast.op == '::':
            if ExpUtils.isNotStringLit(left) or ExpUtils.isNotStringLit(right):
                raise TypeMismatchInExpression(ast)
            return StringType()

    def visitUnExpr(self, ast: UnExpr, c):
        val = self.visit(ast.val, c)
        if ast.op == '!':
            if ExpUtils.isNotBoolLit(val):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if ast.op == '-':
            if ExpUtils.isNotIntFloatLit(val):
                raise TypeMismatchInExpression(ast)
            return IntegerType() if type(val) is IntegerType else FloatType()

    def visitId(self, ast: Id, c):
        global_env = c[0]
        name = ast.name
        for x in global_env:
            if name in x:
                return x[name]['typ']
        raise Undeclared(Identifier(), name)

    def visitArrayCell(self, ast: ArrayCell, c):
        pass

    def visitFuncCall(self, ast, c):
        pass

    def visitBlockStmt(self, ast, c):
        pass

    def visitIfStmt(self, ast, c):
        pass

    def visitForStmt(self, ast, c):
        pass

    def visitWhileStmt(self, ast, c):
        pass

    def visitDoWhileStmt(self, ast, c):
        pass

    def visitContinueStmt(self, ast, c):
        pass

    def visitBreakStmt(self, ast, c):
        pass

    def visitReturnStmt(self, ast, c):
        pass

    def visitAssignStmt(self, ast, c):
        pass

    def visitCallStmt(self, ast, c):
        pass

    def visitIntegerLit(self, ast: IntegerLit, c):
        return IntegerType()

    def visitFloatLit(self, ast: FloatLit, c):
        return FloatType()

    def visitBooleanLit(self, ast: BooleanLit, c):
        return BooleanType()

    def visitStringLit(self, ast: StringLit, c):
        return StringType()

    def visitArrayLit(self, ast: ArrayLit, c):
        (global_env, array_ast) = c
        value_lst = list(map(lambda x: self.visit(
            x, (global_env, array_ast)), ast.explist))
        # value_lst: [IntegerType(...), ArrayTyp(...)]
        print(value_lst)

        if len(ast.explist) == 0:
            return ArrayTyp(0, array_ast.typ)

        first_el_type = value_lst[0]
        if ExpUtils.isArrayLit(first_el_type):
            maximum_val = first_el_type
            for i in value_lst:
                # Check all elements in one array_lit have the same array_type
                if not ExpUtils.isTheSameType(first_el_type, i):
                    raise IllegalArrayLiteral(ast)
                # {{1}, {1, 2, 3}} -> ArrayTyp(2,ArrayTyp(3,IntegerType))
                if i.num_of_el > first_el_type.num_of_el:
                    maximum_val = i
            return ArrayTyp(len(value_lst), maximum_val)

        for i in value_lst:
            # Check all elements in one array_lit have the same automic_type
            if not ExpUtils.isTheSameType(first_el_type, i):
                raise IllegalArrayLiteral(ast)
            # Check each type element in array_lit is similar with type of array_type
            i = TypUtils.impConversion(
                array_ast.typ, i, lambda: self.setIlligalArrayLit(True))
            if not ExpUtils.isTheSameType(i, array_ast.typ):
                self.illegal_array_lit = True
        # {1, 2, 3} -> ArrayTyp(3,IntegerType)
        return ArrayTyp(len(value_lst), first_el_type)
