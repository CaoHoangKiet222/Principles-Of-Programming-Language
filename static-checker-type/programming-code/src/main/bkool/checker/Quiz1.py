from AST import *
from Visitor import *
from StaticError import *


class ExpUtils:
    @staticmethod
    def isNotIntFloatLit(expr):
        return type(expr) not in [IntType, FloatType]

    @staticmethod
    def isNotBoolLit(expr):
        return type(expr) is not BoolType


class Quiz1Checker(BaseVisitor):
    def visitBinOp(self, ctx: BinOp, o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-', '*', '/']:
            if ExpUtils.isNotIntFloatLit(e1) or ExpUtils.isNotIntFloatLit(e2):
                raise TypeMismatchInExpression(ctx)
            if ctx.op == '/':
                return FloatType()
            else:
                if FloatType in [type(e1), type(e2)]:
                    return FloatType()
                else:
                    return IntType()
        if ctx.op in ['<', '>', '==', '!=']:
            if type(e1) is not type(e2):
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if ctx.op in ['&&', '||']:
            if ExpUtils.isNotBoolLit(e1) or ExpUtils.isNotBoolLit(e2):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self, ctx: UnOp, o):
        e = self.visit(ctx.e, o)
        if ctx.op == '-':
            if ExpUtils.isNotIntFloatLit(e):
                raise TypeMismatchInExpression(ctx)
        if ctx.op == '!':
            if ExpUtils.isNotBoolLit(e):
                raise TypeMismatchInExpression(ctx)
        return e

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()
