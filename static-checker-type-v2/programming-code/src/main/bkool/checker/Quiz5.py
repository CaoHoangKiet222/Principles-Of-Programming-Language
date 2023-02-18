from AST import *
from Visitor import *
from StaticError import *


def isFunction(args):
    return isinstance(args, dict)


def infer_with_index(id: str, type, index, o):
    for env in o:
        if id in env:
            if env[id]["params"][index] is None:
                env[id]["params"][index] = type
                return type
            else:
                return env[id]["params"][index]
    return None


def infer(id: Id, type, o):
    for env in o:
        if id.name in env:
            if env[id.name] is None:
                env[id.name] = type
                return type
            else:
                return env[id.name]
    return None


class Quiz5Checker(BaseVisitor):
    def visitProgram(self, ctx: Program, o):
        o = [{}]
        for decl in ctx.decl:
            self.visit(decl, o)
        for stmt in ctx.stmts:
            self.visit(stmt, o)
        return ""

    def visitVarDecl(self, ctx: VarDecl, o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = None  # IntType | FloatType
        return ctx.name

    def visitFuncDecl(self, ctx: FuncDecl, o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        env = [{}] + o
        o[0][ctx.name] = {
            "params": [],  # [IntType, FloatType]
            "typ": None
        }
        params = []
        for param in ctx.param:
            params.append(self.visit(param, env))
        for local in ctx.local:
            self.visit(local, env)
        for stmt in ctx.stmts:
            self.visit(stmt, env)
        for index in range(0, len(ctx.param)):
            typ = env[0][params[index]]
            o[0][ctx.name]["params"].append(typ)

    def visitAssign(self, ctx: Assign, o):
        lhs = self.visit(ctx.lhs, o)
        rhs = self.visit(ctx.rhs, o)
        if type(lhs) is type(None) and type(rhs) is type(None):
            raise TypeCannotBeInferred(ctx)
        if type(lhs) is type(None):
            lhs = infer(ctx.lhs, rhs, o)
        if type(rhs) is type(None):
            rhs = infer(ctx.rhs, lhs, o)
        if type(lhs) is not type(rhs):
            raise TypeMismatchInStatement(ctx)

    def visitCallStmt(self, ctx: CallStmt, o):
        res = self.visitId(Id(ctx.name), o)
        if isFunction(res):
            if len(res["params"]) != len(ctx.args):
                raise TypeMismatchInStatement(ctx)

            for index, arg in enumerate(ctx.args):
                typ_arg = self.visit(arg, o)
                if type(typ_arg) is type(None) and type(res["params"][index]) is type(None):
                    raise TypeCannotBeInferred(ctx)
                if type(typ_arg) is type(None):
                    typ_arg = infer(arg, res["params"][index], o)
                if type(res["params"][index]) is type(None):
                    typ_arg = infer_with_index(ctx.name, typ_arg, index, o)
                if type(typ_arg) is not type(res["params"][index]):
                    raise TypeMismatchInStatement(ctx)
            return
        else:
            raise UndeclaredIdentifier(ctx.name)

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

    def visitId(self, ctx, o):
        for env in o:
            if ctx.name in env:
                return env[ctx.name]
        raise UndeclaredIdentifier(ctx.name)
