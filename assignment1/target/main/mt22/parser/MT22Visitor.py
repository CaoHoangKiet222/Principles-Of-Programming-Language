# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_list.
    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#body.
    def visitBody(self, ctx:MT22Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_decl.
    def visitType_decl(self, ctx:MT22Parser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#non_auto_type_decl.
    def visitNon_auto_type_decl(self, ctx:MT22Parser.Non_auto_type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_type.
    def visitInt_type(self, ctx:MT22Parser.Int_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#float_type.
    def visitFloat_type(self, ctx:MT22Parser.Float_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolean_type.
    def visitBoolean_type(self, ctx:MT22Parser.Boolean_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_type.
    def visitString_type(self, ctx:MT22Parser.String_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element_type.
    def visitElement_type(self, ctx:MT22Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#void_type.
    def visitVoid_type(self, ctx:MT22Parser.Void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#auto_type.
    def visitAuto_type(self, ctx:MT22Parser.Auto_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_lit.
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stat.
    def visitStat(self, ctx:MT22Parser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stat.
    def visitAssign_stat(self, ctx:MT22Parser.Assign_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stat.
    def visitIf_stat(self, ctx:MT22Parser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_part.
    def visitIf_part(self, ctx:MT22Parser.If_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#else_part.
    def visitElse_part(self, ctx:MT22Parser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stat.
    def visitFor_stat(self, ctx:MT22Parser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_var.
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#condition_expr.
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stat.
    def visitWhile_stat(self, ctx:MT22Parser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stat.
    def visitDo_while_stat(self, ctx:MT22Parser.Do_while_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stat.
    def visitBreak_stat(self, ctx:MT22Parser.Break_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stat.
    def visitContinue_stat(self, ctx:MT22Parser.Continue_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stat.
    def visitReturn_stat(self, ctx:MT22Parser.Return_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stat.
    def visitCall_stat(self, ctx:MT22Parser.Call_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_name.
    def visitFunc_name(self, ctx:MT22Parser.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stat_exprs.
    def visitCall_stat_exprs(self, ctx:MT22Parser.Call_stat_exprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stat.
    def visitBlock_stat(self, ctx:MT22Parser.Block_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#body_block_stat.
    def visitBody_block_stat(self, ctx:MT22Parser.Body_block_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list_for_valdecl.
    def visitExpr_list_for_valdecl(self, ctx:MT22Parser.Expr_list_for_valdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list.
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_op.
    def visitIndex_op(self, ctx:MT22Parser.Index_opContext):
        return self.visitChildren(ctx)



del MT22Parser