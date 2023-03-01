from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce


class ASTGenQuiz1(BKOOLVisitor):
    # program: mptype EOF;
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return ctx.mptype().accept(self)

    # mptype: primtype | arraytype;
    def visitMptype(self, ctx: BKOOLParser.MptypeContext):
        return ctx.getChild(0).accept(self)

    # arraytype: primtype dimens;
    def visitArraytype(self, ctx: BKOOLParser.ArraytypeContext):
        return ArrayType(ctx.dimens().accept(self), ctx.primtype().accept(self))

    # primtype: INTTYPE | FLOATTYPE;
    def visitPrimtype(self, ctx: BKOOLParser.PrimtypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # dimens: dimen+;
    def visitDimens(self, ctx: BKOOLParser.DimensContext):
        return reduce(lambda x, y: UnionType(x, y.accept(self)), ctx.dimen()[1:], ctx.dimen(0).accept(self))

    # dimen: '[' num '..' num ']';
    def visitDimen(self, ctx: BKOOLParser.DimenContext):
        return RangeType(ctx.num(0).accept(self), ctx.num(1).accept(self))

    # num: '-'? INTLIT;
    def visitNum(self, ctx: BKOOLParser.DimenContext):
        return int(ctx.INTLIT().getText()) if ctx.getChildCount() == 1 else -int(ctx.INTLIT().getText())
