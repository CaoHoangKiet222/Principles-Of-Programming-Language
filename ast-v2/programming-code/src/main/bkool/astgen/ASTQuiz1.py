from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class ASTGenQuiz1(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return ctx.exp().accept(self)

    def visitExp(self, ctx: BKOOLParser.ExpContext):
        if ctx.ASSIGN():
            return Binary(ctx.ASSIGN().getText(), ctx.term().accept(self), ctx.exp().accept(self))
        return ctx.term().accept(self)

    def visitTerm(self, ctx: BKOOLParser.TermContext):
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))
        return ctx.factor(0).accept(self)

    def visitFactor(self, ctx: BKOOLParser.FactorContext):
        if ctx.ANDOR():
            return Binary(ctx.ANDOR().getText(), ctx.factor().accept(self), ctx.operand().accept(self))
        return ctx.operand().accept(self)

    def visitOperand(self, ctx: BKOOLParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())

        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())

        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())

        return ctx.exp().accept(self)
