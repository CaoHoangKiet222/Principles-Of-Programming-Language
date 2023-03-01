from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class ASTGeneration(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        res = []
        for vardec in ctx.vardecl():
            res += vardec.accept(self)
        return Program(res)

    def visitVardecl(self, ctx: BKOOLParser.VardeclContext):
        res = []
        ids = ctx.ids().accept(self)
        for id in ids:
            res.append(VarDecl(id, ctx.mptype().accept(self)))
        return res

    def visitMptype(self, ctx: BKOOLParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitIds(self, ctx: BKOOLParser.IdsContext):
        if ctx.COMMA():
            return [Id(id.getText()) for id in ctx.ID()]
        return [Id(ctx.ID(0).getText())]
