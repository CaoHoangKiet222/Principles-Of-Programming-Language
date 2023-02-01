from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser


# Count the non-terminal nodes in the parse tree
class ASTQuiz2Generation(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return ctx.vardecls().accept(self) + 2

    def visitVardecls(self, ctx: BKOOLParser.VardeclsContext):
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self) + 2

    def visitVardecltail(self, ctx: BKOOLParser.VardecltailContext):
        if ctx.getChildCount() == 2:
            return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self) + 2
        return 0

    def visitVardecl(self, ctx: BKOOLParser.VardeclContext):
        return ctx.mptype().accept(self) + ctx.ids().accept(self) + 2

    def visitMptype(self, ctx: BKOOLParser.MptypeContext):
        return 0

    def visitIds(self, ctx: BKOOLParser.IdsContext):
        if ctx.getChildCount() == 3:
            return 1 + ctx.ids().accept(self)
        return 0
