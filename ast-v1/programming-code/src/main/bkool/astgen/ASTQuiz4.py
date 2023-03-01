from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


# Return the height of the parse tree
class ASTQuiz4Generation(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return ctx.vardecls().accept(self) + 1

    def visitVardecls(self, ctx: BKOOLParser.VardeclsContext):
        hvd = ctx.vardecl().accept(self)
        hvdt = ctx.vardecltail().accept(self)
        return (hvd if hvd > hvdt else hvdt) + 1

    def visitVardecltail(self, ctx: BKOOLParser.VardecltailContext):
        if ctx.getChildCount() == 2:
            hvd = ctx.vardecl().accept(self)
            hvdt = ctx.vardecltail().accept(self)
            return (hvd if hvd > hvdt else hvdt) + 1
        return 0

    def visitVardecl(self, ctx: BKOOLParser.VardeclContext):
        hmp = ctx.mptype().accept(self)
        hids = ctx.ids().accept(self)
        return (hmp if hmp > hids else hids) + 1

    def visitMptype(self, ctx: BKOOLParser.MptypeContext):
        return 1

    def visitIds(self, ctx: BKOOLParser.IdsContext):
        if ctx.getChildCount() == 3:
            return 1 + ctx.ids().accept(self)
        return 1
