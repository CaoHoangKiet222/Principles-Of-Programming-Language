from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


# Generate the AST of a MP input
class ASTQuiz3Generation(BKOOLVisitor):
    # program: vardecls EOF;
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program(ctx.vardecls().accept(self))

    def visitVardecls(self, ctx: BKOOLParser.VardeclsContext):
        return [ctx.vardecl().accept(self), *ctx.vardecltail().accept(self)]

    def visitVardecltail(self, ctx: BKOOLParser.VardecltailContext):
        return [ctx.vardecl().accept(self), *ctx.vardecltail().accept(self)
                ] if ctx.getChildCount() == 2 else []

    def visitVardecl(self, ctx: BKOOLParser.VardeclContext):
        ids = ctx.ids().accept(self)
        return ','.join(str(VarDecl(id, ctx.mptype().accept(self))) for id in ids)

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self, ctx: BKOOLParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # ids: ID ',' ids | ID;
    def visitIds(self, ctx: BKOOLParser.IdsContext):
        return [Id(ctx.ID().getText()), *ctx.ids().accept(self)] if ctx.getChildCount() == 3 else [Id(ctx.ID().getText())]
