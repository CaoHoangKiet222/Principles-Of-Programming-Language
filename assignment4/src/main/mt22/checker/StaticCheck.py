"""
 * @author nhphung
 * Student's name: Cao Hoang Kiet
 * Student's ID: 2053165
"""

from typing import List, Tuple
from AST import *
from Utils import *
from Visitor import *
from StaticError import *
from functools import reduce


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self) -> str:
        return "MType({},{})".format(str(self.partype), str(self.rettype))


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

    def __str__(self) -> str:
        return "Symbol({},{},{})".format(str(self.name), str(self.mtype), str(self.value) if self.value else "")


class CheckUtils:
    @staticmethod
    def dimensionsMatch(dimensions1: List[int], dimensions2: List[int]):
        if dimensions2[0] == 0:
            return True
        if len(dimensions1) != len(dimensions2):
            return False
        for idx, i in enumerate(dimensions1):
            if i < dimensions2[idx]:
                return False
        return True

    @staticmethod
    def redeclaredParams(params1, params2, error):
        for key in params1:
            if key in params2:
                raise error(key)

    @staticmethod
    def inLoop(ob):
        if len(ob["for"]) != 0 or len(ob["while"]) != 0 or len(ob["dowhile"]) != 0:
            return True
        return False


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
    def impConversion(lhs_typ: Type, rhs_typ: Type, callback):
        if type(lhs_typ) is IntegerType:
            if type(rhs_typ) is FloatType:
                callback()
                return
        elif type(lhs_typ) is FloatType:
            if type(rhs_typ) is IntegerType:
                return FloatType()
        return rhs_typ


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


def retriveEl(name: str, o, callback):
    for env in o:
        if name in env:
            return env[name]
    return callback()


def retriveElWithCond(name: str, o, cond, callback):
    for env in o:
        if name in env and cond(env):
            return env[name]
    return callback()


def retriveInheritParams(name: str, o):
    for env in o:
        if name in env and isinstance(env[name]["kind"], Function):
            inherit_name = env[name]["inherit"]
            params_inherit = retriveInheritParams(inherit_name, o)
            CheckUtils.redeclaredParams(
                params_inherit, env[name]["params_inherit"], lambda e: Redeclared(
                    Parameter(), e)
            )
            return {**params_inherit, **env[name]["params_inherit"]}
    return {}


class StaticChecker(BaseVisitor, Utils):
    global_envi = [
        Symbol("readInteger", MType([], IntegerType())),
        Symbol("printInteger", MType([IntegerType()], VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("writeFloat", MType([FloatType()], VoidType())),
        Symbol("readBoolean", MType([], BooleanType())),
        Symbol("printBoolean", MType([BooleanType()], VoidType())),
        Symbol("readString", MType([], StringType())),
        Symbol("printString", MType([StringType()], VoidType())),
        Symbol("super", MType([List[Expr]], VoidType())),
        Symbol("preventDefault", MType([], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast
        self.global_env = [{}]
        self.current_method = {}
        self.checkInherit = False
        self.illegal_array_lit = False
        self.init = {
            "error": False,
            "forloop": False,
        }
        self.inloop = {
            "for": [],
            "while": [],
            "dowhile": []
        }

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)

    def setIlligalArrayLit(self, value):
        self.illegal_array_lit = value

    def __raise(self, ex):
        raise ex

    def checkParamsMatch(self, args, params, c):
        # params: LHS, args: RHS
        (global_env, infer_typ, error) = c
        for x in zip(args, params):
            typ = None
            if type(x[0]) is FuncCall:
                # Infer from parameter
                typ = self.visit(x[0], (global_env, x[1]))
            else:
                typ = self.visit(x[0], (global_env, infer_typ))
            # Check error when implicit conversion --> Case: float / integer
            typ = TypUtils.impConversion(
                x[1], typ, lambda: self.__raise(error))
            # Check arguments and parameters have the same type
            if not ExpUtils.isTheSameType(typ, x[1]):
                self.__raise(error)

    def visitProgram(self, ast: Program, c):
        # decls: List[Decl]
        # c has structure
        # [
        #   {
        #      variable_name: {"kind": Variable/Parameter, "typ": Type},
        #      method_name: {"kind": Function, "typ": Type, "params": [Type]},
        #   }
        # ]
        # global_env need to be passed when visit stmt and decls
        # (global_env, infer_typ) need to be passed when visit expr
        c = self.global_env
        for sym in self.global_envi:
            c[0][sym.name] = {
                "kind": Function(), "typ": sym.mtype.rettype, "params": sym.mtype.partype
            }
        flag = False
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                # change this if error
                if decl.name.name == "main" and type(decl.return_type) is VoidType and len(decl.params) == 0:
                    flag = True
            elif type(decl) is ParamDecl:
                # change this if error
                raise Invalid(Parameter(), decl.name.name)
            self.visit(decl, c)

        if flag == False:
            raise NoEntryPoint()
        return ""

    def visitVarDecl(self, ast: VarDecl, c):
        print("========================== VarDecl", ast)
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
                # Check dimensions initialization match with its array_type_dimensions
                if not CheckUtils.dimensionsMatch(typ.dimensions, TypUtils.retriveDimensions(init_typ)):
                    raise TypeMismatchInStatement(ast)
            else:
                init_typ = self.visit(init, (c, typ))
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
        # Declared in type auto without the initialization.
        elif type(typ) is AutoType:
            raise Invalid(Variable(), name)

        c[0][name] = {"kind": Variable(), "typ": typ}
        print("========================== End VarDecl")

    def visitParamDecl(self, ast: ParamDecl, c):
        print("========================== ParamDecl", ast)
        global_env = c
        name = ast.name.name  # change this if error
        typ = ast.typ
        out = ast.out
        inherit = ast.inherit
        if name in global_env[0]:
            raise Redeclared(Parameter(), name)
        global_env[0][name] = {
            "kind": Parameter(), "typ": typ, "out": out, "inherit": inherit
        }
        print(global_env)
        if inherit == True:
            self.current_method["params_inherit"][name] = {
                "kind": Parameter(), "typ": typ, "out": out
            }
        self.current_method["params"].append(typ)
        print("========================== End ParamDecl")

    def visitFuncDecl(self, ast: FuncDecl, c):
        print("=========================== FuncDecl", ast)
        # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
        name = ast.name.name  # change this if error
        return_type = ast.return_type
        params = ast.params
        inherit = ast.inherit  # change this if error
        body = ast.body

        if name in c[0]:
            raise Redeclared(Function(), name)
        env = [{}] + c
        self.current_method = c[0][name] = {
            "kind": Function(), "typ": return_type, "params": [], "params_inherit": {}, "inherit": inherit.name if inherit else None, "inherit_checked": False
        }
        reduce(lambda _, p: self.visit(p, env), params, [])
        if inherit is not None:
            inherit = inherit.name  # change this if error
            parent_func = retriveElWithCond(
                inherit, env, lambda el: isinstance(el[name]["kind"], Function), lambda: self.__raise(
                    Undeclared(Function(), inherit))
            )
            # check no stmts in funcdecl body
            if len(body.body) == 0 and len(parent_func["params"]) != 0:
                raise InvalidStatementInFunction(name)
            first_stmt = body.body[0]
            if type(first_stmt) is CallStmt:
                # change this if error
                sym = self.lookup(first_stmt.name.name,
                                  StaticChecker.global_envi, lambda x: x.name)
                # check first_stmt is preventDefault or super
                if sym.name != "preventDefault" and sym.name != "super":
                    if len(parent_func["params"]) != 0:
                        raise InvalidStatementInFunction(name)
                    else:
                        self.visit(first_stmt, env)
                else:
                    if len(parent_func["params"]) == 0:
                        if len(first_stmt.args) != 0:
                            raise InvalidStatementInFunction(name)
                    else:
                        # first_stmt is super
                        if sym.name == "super":
                            if len(first_stmt.args) != len(parent_func["params"]):
                                raise InvalidStatementInFunction(name)
                            self.checkParamsMatch(
                                first_stmt.args, parent_func["params"], (env, None, InvalidStatementInFunction(name)))
                        else:
                            if len(first_stmt.args) != 0:
                                raise InvalidStatementInFunction(name)
                    # Inherit all params from parent function including hierarchical
                    if sym.name == "super":
                        inherit_params = retriveInheritParams(inherit, env)
                        CheckUtils.redeclaredParams(
                            inherit_params, env[0], lambda e: Redeclared(
                                Parameter(), e)
                        )
                        env[0] = {**env[0], **inherit_params}
            # Check activation of parent function is implicit with super
            elif len(parent_func["params"]) != 0:
                raise InvalidStatementInFunction(name)
        self.current_method["inherit_checked"] = True
        self.visit(body, (env, None))  # (global_env, infer_typ)
        print("=========================== End FuncDecl")

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
        (global_env, infer_typ) = c
        left = ast.left
        right = ast.right
        if type(left) is FuncCall and type(right) is FuncCall:
            left_name = left.name.name  # change this if error
            right_name = right.name.name  # change this if error
            func_left = retriveEl(left_name, global_env, lambda: self.__raise(
                Undeclared(Function(), left_name)))
            func_right = retriveEl(right_name, global_env, lambda: self.__raise(
                Undeclared(Function(), right_name)))
            if isinstance(func_left["typ"], AutoType) and not isinstance(func_right["typ"], AutoType):
                right = self.visit(right, c)
                left = self.visit(left, (global_env, right))
            elif isinstance(func_right["typ"], AutoType) and not isinstance(func_left["typ"], AutoType):
                left = self.visit(left, c)
                right = self.visit(right, (global_env, left))
            else:
                left = self.visit(left, c)
                right = self.visit(right, c)
        elif type(left) is FuncCall and type(right) is not FuncCall:
            right = self.visit(right, c)
            left = self.visit(left, (global_env, right))
        elif type(right) is FuncCall and type(left) is not FuncCall:
            left = self.visit(left, c)
            right = self.visit(right, (global_env, left))
        else:
            left = self.visit(left, c)
            right = self.visit(right, c)

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
        (global_env, infer_typ) = c
        val = self.visit(ast.val, (global_env, infer_typ))
        if ast.op == '!':
            if ExpUtils.isNotBoolLit(val):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if ast.op == '-':
            if ExpUtils.isNotIntFloatLit(val):
                raise TypeMismatchInExpression(ast)
            return IntegerType() if type(val) is IntegerType else FloatType()

    def visitId(self, ast: Id, c):
        global_env = c
        # check c is pass from array_lit
        if type(c) is tuple:
            global_env = c[0]
        el = retriveEl(ast.name, global_env, lambda: self.__raise(
            Undeclared(Identifier(), ast.name)))
        return el["typ"]

    def visitArrayCell(self, ast: ArrayCell, c):
        # change this if error
        print("======================= ArrayCell", ast)
        print(c)
        typ = self.visit(ast.name, c)
        # check index operator E1[E2] (E1 must be in array type)
        if type(typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        # check index operator E1[E2] (E2 must be in list of int type)
        reduce(lambda _, x: self.__raise(TypeMismatchInExpression(ast))
               if ExpUtils.isNotIntLit(self.visit(x, c)) else [], ast.cell, [])
        print("======================= End ArrayCell")
        return typ.typ

    def visitFuncCall(self, ast: FuncCall, c):
        print("====================== FuncCall", ast)
        (global_env, infer_typ) = c
        name = ast.name.name  # change this if error
        args = ast.args
        el = None
        for env in global_env:
            if name in env:
                if isinstance(env[name]["kind"], Function):
                    el = env[name]
                    print("++++++++++", el)
                    # Check function call is non_void_type + arguments and parameters need to be the same length
                    if isinstance(el["typ"], VoidType) or len(el["params"]) != len(args):
                        raise TypeMismatchInExpression(ast)
                    self.checkParamsMatch(
                        args, el["params"], (global_env, infer_typ, TypeMismatchInExpression(ast)))
        if el is None:
            raise Undeclared(Function(), name)
        # Infer return of function
        if isinstance(el["typ"], AutoType):
            el["typ"] = infer_typ
        print("====================== End FuncCall", el["typ"])
        return el["typ"]

    def visitBlockStmt(self, ast: BlockStmt, c):
        print("====================== BlockStmt")
        # Check c passed from funcdecl
        pass_from_func = False
        if type(c) is tuple:
            # Do not increase scope when c is passed from funcdecl
            env = c[0]
            pass_from_func = True
        else:
            env = [{}] + c
        if pass_from_func == True and self.current_method["inherit"] is not None:
            list(map(lambda x: self.visit(x, env), ast.body[1:]))
        else:
            list(map(lambda x: self.visit(x, env), ast.body))
        print("====================== End BlockStmt")

    def visitIfStmt(self, ast: IfStmt, c):
        print("================== IfStmt", ast)
        global_env = c
        cond = self.visit(ast.cond, (global_env, None))
        if ExpUtils.isNotBoolLit(cond):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt, global_env)
        if ast.fstmt is not None:
            self.visit(ast.fstmt, global_env)
        print("================== End IfStmt")

    def visitForStmt(self, ast: ForStmt, c):
        print("================== ForStmt", ast)
        # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt

        global_env = c
        env = [{}] + global_env
        self.init["forloop"] = True
        self.inloop["for"].append(True)
        self.visit(ast.init, env)
        # Check init for loop error
        if self.init["error"] == True:
            raise TypeMismatchInStatement(ast)
        self.init["forloop"] = False
        cond = self.visit(ast.cond, (env, BooleanType()))
        # Check cond is BooleanType
        if ExpUtils.isNotBoolLit(cond):
            raise TypeMismatchInStatement(ast)
        upd = self.visit(ast.upd, (env, IntegerType()))
        # Check update is IntegerType
        if ExpUtils.isNotIntLit(upd):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, env)
        self.inloop["for"].pop()
        print("================== End ForStmt")

    def visitWhileStmt(self, ast: WhileStmt, c):
        print("================== WhileStmt", ast)
        # cond: Expr, stmt: Stmt

        global_env = c
        self.inloop["while"].append(True)
        cond = self.visit(ast.cond, (global_env, BooleanType()))
        print("+++++++++++++++++++++", cond)
        # Check cond is BooleanType
        if ExpUtils.isNotBoolLit(cond):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, global_env)
        self.inloop["while"].pop()
        print("================== End WhileStmt")

    def visitDoWhileStmt(self, ast: DoWhileStmt, c):
        print("================== DoWhileStmt", ast)
        # cond: Expr, stmt: Stmt

        global_env = c
        self.inloop["dowhile"].append(True)
        self.visit(ast.stmt, global_env)
        cond = self.visit(ast.cond, (global_env, BooleanType()))
        # Check cond is BooleanType
        if ExpUtils.isNotBoolLit(cond):
            raise TypeMismatchInStatement(ast)
        self.inloop["dowhile"].pop()
        print("================== End DoWhileStmt")

    def visitContinueStmt(self, ast: ContinueStmt, c):
        print("================== ContinueStmt", self.inloop)
        if not CheckUtils.inLoop(self.inloop):
            raise MustInLoop(ast)
        print("================== End ContinueStmt")

    def visitBreakStmt(self, ast: BreakStmt, c):
        if not CheckUtils.inLoop(self.inloop):
            raise MustInLoop(ast)

    def visitReturnStmt(self, ast: ReturnStmt, c):
        print("============== ReturnStmt", ast)
        global_env = c
        if ast.expr is not None:
            rhs_typ = self.visit(ast.expr, (global_env, None))
            print("++++++++++++++++++++++++++++", rhs_typ)
        else:
            rhs_typ = VoidType()
        # Check error when implicit conversion --> Case: float / integer
        rhs_typ = TypUtils.impConversion(
            self.current_method["typ"], rhs_typ, lambda: self.__raise(
                TypeMismatchInExpression(ast)))
        # Need to infer return_typ with expr
        if type(self.current_method["typ"]) is AutoType:
            self.current_method["typ"] = rhs_typ
        # Check type element in automic_lit is similar with type of its type
        if not ExpUtils.isTheSameType(rhs_typ, self.current_method["typ"]):
            raise TypeMismatchInStatement(ast)

        print("============== End ReturnStmt")

    def visitAssignStmt(self, ast: AssignStmt, c):
        print("============== AssignStmt", ast)
        global_env = c
        if self.init["forloop"] == True:
            name = ast.lhs.name  # change this if error
            try:
                el = retriveEl(name, global_env, lambda: self.__raise(
                    Undeclared(Variable(), name)))
                # Check the type of scalar variable must be integer in for loop
                if not isinstance(el["typ"], IntegerType):
                    self.init["error"] = True
                    return
                lhs_typ = el["typ"]
            except Undeclared:
                lhs_typ = IntegerType()
                global_env[0][name] = {"kind": Variable(), "typ": lhs_typ}

            rhs_typ = self.visit(ast.rhs, (global_env, lhs_typ))
            if ExpUtils.isNotIntLit(rhs_typ):
                self.init["error"] = True
                return
        else:
            lhs_typ = self.visit(ast.lhs, global_env)
            # Check left-hand side is void type or array type
            if type(lhs_typ) is ArrayType or type(lhs_typ) is VoidType:
                raise TypeMismatchInStatement(ast)

            rhs_typ = self.visit(ast.rhs, (global_env, lhs_typ))
            # Check element type coercion
            rhs_typ = TypUtils.impConversion(
                lhs_typ, rhs_typ, lambda: self.__raise(TypeMismatchInExpression(ast)))
            if not ExpUtils.isTheSameType(lhs_typ, rhs_typ):
                raise TypeMismatchInStatement(ast)
        print("============== End AssignStmt")

    def visitCallStmt(self, ast: CallStmt, c):
        print("====================== CallStmt", ast)
        global_env = c
        name = ast.name.name  # change this if error
        args = ast.args
        el = None

        for env in global_env:
            if name in env:
                if isinstance(env[name]["kind"], Function):
                    el = env[name]
                    # Check current function has super or preventDefault method with no inherit
                    inherit = self.current_method["inherit"]
                    if inherit is None:
                        if name == "super" or name == "preventDefault":
                            raise TypeMismatchInStatement(ast)
                    else:
                        if not self.current_method["inherit_checked"]:
                            parent_func = retriveElWithCond(
                                inherit, global_env, lambda el: isinstance(el[name]["kind"], Function), lambda: self.__raise(
                                    Undeclared(Function(), inherit))
                            )
                            if name != "preventDefault" and name != "super":
                                if len(parent_func["params"]) != 0:
                                    raise TypeMismatchInStatement(ast)

                    # Infer return of function
                    if isinstance(el["typ"], AutoType):
                        el["typ"] = VoidType()
                    # Check callstmt is void_type + arguments and parameters need to be the same length
                    if (not isinstance(el["typ"], VoidType)) or len(el["params"]) != len(args):
                        raise TypeMismatchInStatement(ast)
                    self.checkParamsMatch(
                        args, el["params"], (global_env, None, TypeMismatchInStatement(ast)))
        if el is None:
            raise Undeclared(Function(), name)
        print("====================== End CallStmt")

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
