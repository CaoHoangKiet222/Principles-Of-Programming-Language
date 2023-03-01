from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce


class ASTGenQuiz2(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx: BKOOLParser.ExpContext):
        # ele = (ASSIGN, term)
        rvt = ctx.term()[::-1]
        arv = ctx.ASSIGN()[::-1]
        return reduce(lambda acc, ele: Binary(ele[0].getText(), ele[1].accept(self), acc), zip(arv, rvt[1:]), rvt[0].accept(self))

    def visitTerm(self, ctx: BKOOLParser.TermContext):
        return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1))) if ctx.getChildCount() == 3 else self.visit(ctx.factor(0))

    def visitFactor(self, ctx: BKOOLParser.FactorContext):
        # ele = (ANDOR, term)
        return reduce(lambda acc, ele: Binary(ele[0].getText(), acc, ele[1].accept(self)), zip(ctx.ANDOR(), ctx.operand()[1:]), ctx.operand(0).accept(self))

    def visitOperand(self, ctx: BKOOLParser.OperandContext):
        return IntLiteral(ctx.INTLIT().getText()) if ctx.INTLIT() else Id(ctx.ID().getText()) if ctx.ID() else BooleanLiteral(ctx.BOOLIT().getText()) if ctx.BOOLIT() else self.visit(ctx.exp())
