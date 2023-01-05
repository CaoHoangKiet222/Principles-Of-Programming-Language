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