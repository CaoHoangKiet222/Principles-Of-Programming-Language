# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#program_int.
    def visitProgram_int(self, ctx:BKOOLParser.Program_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdecl.
    def visitFuncdecl(self, ctx:BKOOLParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body_stats.
    def visitBody_stats(self, ctx:BKOOLParser.Body_statsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stats.
    def visitStats(self, ctx:BKOOLParser.StatsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stat.
    def visitAssign_stat(self, ctx:BKOOLParser.Assign_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call_stat.
    def visitCall_stat(self, ctx:BKOOLParser.Call_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call_stat_exprs.
    def visitCall_stat_exprs(self, ctx:BKOOLParser.Call_stat_exprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stat.
    def visitReturn_stat(self, ctx:BKOOLParser.Return_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#identifiers.
    def visitIdentifiers(self, ctx:BKOOLParser.IdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func_args.
    def visitFunc_args(self, ctx:BKOOLParser.Func_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func_name.
    def visitFunc_name(self, ctx:BKOOLParser.Func_nameContext):
        return self.visitChildren(ctx)



del BKOOLParser