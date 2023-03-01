from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce


class ASTGenQuiz2(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return ctx.mptype().accept(self)

    # mptype: primtype | arraytype;
    def visitMptype(self, ctx: BKOOLParser.MptypeContext):
        if ctx.arraytype():
            lst = ctx.arraytype().accept(self)
            return ArrayType(reduce(lambda x, y: UnionType(x, y), lst[2:], lst[1]), lst[0])
        return ctx.getChild(0).accept(self)

    # arraytype: arraytype dimen | primtype dimen;
    def visitArraytype(self, ctx: BKOOLParser.ArraytypeContext):
        if ctx.arraytype():
            return ctx.arraytype().accept(self) + [ctx.dimen().accept(self)]
        return [ctx.primtype().accept(self), ctx.dimen().accept(self)]

    # primtype: INTTYPE | FLOATTYPE;
    def visitPrimtype(self, ctx: BKOOLParser.PrimtypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # dimen: '[' num '..' num ']';
    def visitDimen(self, ctx: BKOOLParser.DimenContext):
        return RangeType(ctx.num(0).accept(self), ctx.num(1).accept(self))

    # num: '-'? INTLIT;
    def visitNum(self, ctx: BKOOLParser.DimenContext):
        return int(ctx.INTLIT().getText()) if ctx.getChildCount() == 1 else -int(ctx.INTLIT().getText())
