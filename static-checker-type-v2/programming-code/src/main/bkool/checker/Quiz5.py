from AST import *
from Visitor import *
from StaticError import *


class ExpUtils:
    @staticmethod
    def isNotIntLit(expr):
        return type(expr) is not IntType

    @staticmethod
    def isNotFloatLit(expr):
        return type(expr) is not FloatType

    @staticmethod
    def isNotBoolLit(expr):
        return type(expr) is not BoolType


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
        o[0][ctx.name] = None

    def visitBlock(self, ctx: Block, o):
        env = [{}] + o
        for decl in ctx.decl:
            self.visit(decl, env)
        for stmt in ctx.stmts:
            self.visit(stmt, env)

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

    def visitBinOp(self, ctx: BinOp, o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-', '*', '/', '>', '=']:
            if type(e1) is type(None):
                e1 = infer(ctx.e1, IntType(), o)
            if type(e2) is type(None):
                e2 = infer(ctx.e2, IntType(), o)
            if ExpUtils.isNotIntLit(e1) or ExpUtils.isNotIntLit(e2):
                raise TypeMismatchInExpression(ctx)
            if ctx.op in ['+', '-', '*', '/']:
                return IntType()
            else:
                return BoolType()
        if ctx.op in ['+.', '-.', '*.', '/.', '>.', '=.']:
            if type(e1) is type(None):
                e1 = infer(ctx.e1, FloatType(), o)
            if type(e2) is type(None):
                e2 = infer(ctx.e2, FloatType(), o)
            if ExpUtils.isNotFloatLit(e1) or ExpUtils.isNotFloatLit(e2):
                raise TypeMismatchInExpression(ctx)
            if ctx.op in ['>.', '=.']:
                return BoolType()
            return FloatType()
        if ctx.op in ['&&', '||', '>b', '=b']:
            if type(e1) is type(None):
                e1 = infer(ctx.e1, BoolType(), o)
            if type(e2) is type(None):
                e2 = infer(ctx.e2, BoolType(), o)
            if ExpUtils.isNotBoolLit(e1) or ExpUtils.isNotBoolLit(e2):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self, ctx: UnOp, o):
        e = self.visit(ctx.e, o)
        if ctx.op in ['-', 'i2f']:
            if type(e) is type(None):
                e = infer(ctx.e, IntType(), o)
            if ExpUtils.isNotIntLit(e):
                raise TypeMismatchInExpression(ctx)
            if ctx.op == 'i2f':
                return FloatType()
            return IntType()
        if ctx.op in ['-.', 'floor']:
            if type(e) is type(None):
                e = infer(ctx.e, FloatType(), o)
            if ExpUtils.isNotFloatLit(e):
                raise TypeMismatchInExpression(ctx)
            if ctx.op == 'floor':
                return IntType()
            return FloatType()
        if ctx.op == '!':
            if type(e) is type(None):
                e = infer(ctx.e, BoolType(), o)
            if ExpUtils.isNotBoolLit(e):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

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
