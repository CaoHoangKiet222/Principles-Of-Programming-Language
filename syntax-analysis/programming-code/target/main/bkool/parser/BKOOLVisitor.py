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


    # Visit a parse tree produced by BKOOLParser#id_list.
    def visitId_list(self, ctx:BKOOLParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#non_auto_type_decl.
    def visitNon_auto_type_decl(self, ctx:BKOOLParser.Non_auto_type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#int_type.
    def visitInt_type(self, ctx:BKOOLParser.Int_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#float_type.
    def visitFloat_type(self, ctx:BKOOLParser.Float_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#boolean_type.
    def visitBoolean_type(self, ctx:BKOOLParser.Boolean_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#string_type.
    def visitString_type(self, ctx:BKOOLParser.String_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#dimensions.
    def visitDimensions(self, ctx:BKOOLParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#element_type.
    def visitElement_type(self, ctx:BKOOLParser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#void_type.
    def visitVoid_type(self, ctx:BKOOLParser.Void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#auto_type.
    def visitAuto_type(self, ctx:BKOOLParser.Auto_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_list.
    def visitExpr_list(self, ctx:BKOOLParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)



del BKOOLParser