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


    # Visit a parse tree produced by BKOOLParser#arraytype.
    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mptype.
    def visitMptype(self, ctx:BKOOLParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primtype.
    def visitPrimtype(self, ctx:BKOOLParser.PrimtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#dimen.
    def visitDimen(self, ctx:BKOOLParser.DimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#num.
    def visitNum(self, ctx:BKOOLParser.NumContext):
        return self.visitChildren(ctx)



del BKOOLParser