from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser


# Count the terminal nodes in the parse tree
class ASTQuiz1Generation(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return ctx.vardecls().accept(self) + 1

    def visitVardecls(self, ctx: BKOOLParser.VardeclsContext):
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecltail(self, ctx: BKOOLParser.VardecltailContext):
        if ctx.getChildCount() == 2:
            return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)
        return 0

    def visitVardecl(self, ctx: BKOOLParser.VardeclContext):
        return ctx.mptype().accept(self) + ctx.ids().accept(self) + 1

    def visitMptype(self, ctx: BKOOLParser.MptypeContext):
        return 1

    def visitIds(self, ctx: BKOOLParser.IdsContext):
        if ctx.getChildCount() == 3:
            return 2 + ctx.ids().accept(self)
        return 1
