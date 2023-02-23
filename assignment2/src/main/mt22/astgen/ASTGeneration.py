from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def check_if_array(self, variable):
        if isinstance(variable, (list, tuple)):
            return True
        else:
            return False

    # program: program_init EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(ctx.decls().accept(self))

    # decls: decl decls| decl;
    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        decls = []
        res = ctx.decl().accept(self)
        if self.check_if_array(res):
            decls.extend(res)
        else:
            decls.append(res)
        if ctx.decls():
            decls.extend(ctx.decls().accept(self))
        return decls

    # decl: vardecl| funcdecl| paramdecl;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return ctx.getChild(0).accept(self)

    def visitParamdecl(self, ctx: MT22Parser.ParamdeclContext):
        return ctx.param().accept(self)

    # funcdecl: func_name COLON FUNCTION return_type LP param_list? RP (INHERIT ID)? body;
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        name = ctx.func_name().accept(self)
        return_type = ctx.return_type().accept(self)
        params = ctx.param_list().accept(self) if ctx.param_list() else []
        inherit = ctx.INHERIT().getText() if ctx.INHERIT() else None
        body = ctx.body().accept(self)
        return FuncDecl(name, return_type, params, inherit, body)

    # return_type: type_decl| void_type;
    def visitReturn_type(self, ctx: MT22Parser.Return_typeContext):
        return ctx.getChild(0).accept(self)

    # param_list: param COMMA param_list| param;
    def visitParam_list(self, ctx: MT22Parser.Param_listContext):
        return [ctx.param().accept(self), *ctx.param_list().accept(self)] if ctx.COMMA() else [ctx.param().accept(self)]

    # param: INHERIT? OUT? ID COLON type_decl;
    def visitParam(self, ctx: MT22Parser.ParamContext):
        return ParamDecl(Id(ctx.ID().getText()), ctx.type_decl().accept(self), True if ctx.OUT() else False, True if ctx.INHERIT() else False)

    # body: block_stat;
    def visitBody(self, ctx: MT22Parser.BodyContext):
        return ctx.block_stat().accept(self)

    # vardecl: id_list COLON type_decl (ASSIGN {self.assign = True} expr_list_for_valdecl)? SEMI
    #  x, y, z: integer = 1, 2, 3; -> Program([
    # 	VarDecl(x, IntegerType, IntegerLit(1))
    # 	VarDecl(y, IntegerType, IntegerLit(2))
    # 	VarDecl(z, IntegerType, IntegerLit(3))
    # ])
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        ids = ctx.id_list().accept(self) if ctx.id_list() else []
        typ = ctx.getChild(2).accept(self)
        exprs = ctx.getChild(4).accept(self) if ctx.ASSIGN() else []

        if len(exprs) == 0:
            return [VarDecl(id, typ) for id in ids]
        return [VarDecl(id, typ, expr) for id, expr in zip(ids, exprs)]

    # id_list: ID COMMA id_list| ID;
    def visitId_list(self, ctx: MT22Parser.Id_listContext):
        return [Id(ctx.ID().getText()), *ctx.id_list().accept(self)] if ctx.id_list() else [Id(ctx.ID().getText())]

    # type_decl: non_auto_type_decl | auto_type;
    def visitType_decl(self, ctx: MT22Parser.Type_declContext):
        return ctx.getChild(0).accept(self)

    # non_auto_type_decl: int_type | float_type | boolean_type | string_type | array_type;
    def visitNon_auto_type_decl(self, ctx: MT22Parser.Non_auto_type_declContext):
        return ctx.getChild(0).accept(self)

    # int_type: INTEGER;
    def visitInt_type(self, ctx: MT22Parser.Int_typeContext):
        return IntegerType()

    # float_type : FLOAT;
    def visitFloat_type(self, ctx: MT22Parser.Float_typeContext):
        return FloatType()

    # boolean_type : BOOLEAN;
    def visitBoolean_type(self, ctx: MT22Parser.Boolean_typeContext):
        return BooleanType()

    # string_type : STRING;
    def visitString_type(self, ctx: MT22Parser.String_typeContext):
        return StringType()

    # array_type: ARRAY LSB dimensions RSB OF element_type;
    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        dimensions = ctx.dimensions().accept(self)
        typ = ctx.element_type().accept(self)
        return ArrayType(dimensions, typ)

    # dimensions: INT_LIT COMMA dimensions| INT_LIT;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        val = ctx.INT_LIT().getText()
        return [val, *ctx.dimensions().accept(self)] if ctx.dimensions() else [val]

    # element_type: int_type | float_type | boolean_type | string_type;
    def visitElement_type(self, ctx: MT22Parser.Element_typeContext):
        return ctx.getChild(0).accept(self)

    # void_type : VOID;
    def visitVoid_type(self, ctx: MT22Parser.Void_typeContext):
        return VoidType()

    # auto_type : AUTO;
    def visitAuto_type(self, ctx: MT22Parser.Auto_typeContext):
        return AutoType()

    # array_lit: LCB expr_list? RCB;
    def visitArray_lit(self, ctx: MT22Parser.Array_litContext):
        explist = ctx.expr_list().accept(self) if ctx.expr_list() else []
        return ArrayLit(explist)

    # stat: assign_stat| if_stat| for_stat| while_stat| do_while_stat| break_stat | continue_stat| return_stat| call_stat| block_stat;
    def visitStat(self, ctx: MT22Parser.StatContext):
        return ctx.getChild(0).accept(self)

    # assign_stat: (scalar_var | ID index_op) ASSIGN expr SEMI;
    def visitAssign_stat(self, ctx: MT22Parser.Assign_statContext):
        lhs = None
        if ctx.scalar_var():
            lhs = ctx.scalar_var().accept(self)
        if ctx.index_op():
            lhs = ArrayCell(Id(ctx.ID().getText()),
                            ctx.index_op().accept(self))
        rhs = ctx.expr().accept(self)
        return AssignStmt(lhs, rhs)

    # if_stat:  if_part else_part?;
    def visitIf_stat(self, ctx: MT22Parser.If_statContext):
        cond = ctx.expr().accept(self)
        tstmt = ctx.stat(0).accept(self)
        fstmt = None
        if ctx.ELSE():
            fstmt = ctx.stat(1).accept(self)
        return IfStmt(cond, tstmt, fstmt)

    # for_stat: FOR LP (scalar_var ASSIGN init_expr) COMMA condition_expr COMMA update_expr RP stat;
    def visitFor_stat(self, ctx: MT22Parser.For_statContext):
        init = AssignStmt(ctx.scalar_var().accept(self),
                          ctx.init_expr().accept(self))
        cond = ctx.condition_expr().accept(self)
        upd = ctx.update_expr().accept(self)
        stmt = ctx.stat().accept(self)
        return ForStmt(init, cond, upd, stmt)

    # scalar_var : ID;
    def visitScalar_var(self, ctx: MT22Parser.Scalar_varContext):
        return Id(ctx.ID().getText())

    # init_expr : expr;
    def visitInit_expr(self, ctx: MT22Parser.Init_exprContext):
        return ctx.expr().accept(self)

    # condition_expr : expr;
    def visitCondition_expr(self, ctx: MT22Parser.Condition_exprContext):
        return ctx.expr().accept(self)

    # update_expr : expr;
    def visitUpdate_expr(self, ctx: MT22Parser.Update_exprContext):
        return ctx.expr().accept(self)

    # while_stat: WHILE LP expr RP stat;
    def visitWhile_stat(self, ctx: MT22Parser.While_statContext):
        cond = ctx.expr().accept(self)
        stmt = ctx.stat().accept(self)
        return WhileStmt(cond, stmt)

    # do_while_stat: DO block_stat WHILE LP expr RP SEMI;
    def visitDo_while_stat(self, ctx: MT22Parser.Do_while_statContext):
        cond = ctx.expr().accept(self)
        stmt = ctx.block_stat().accept(self)
        return WhileStmt(cond, stmt)

    # break_stat: BREAK SEMI;
    def visitBreak_stat(self, ctx: MT22Parser.Break_statContext):
        return BreakStmt()

    # continue_stat: CONTINUE SEMI;
    def visitContinue_stat(self, ctx: MT22Parser.Continue_statContext):
        return ContinueStmt()

    # return_stat: RETURN expr? SEMI;
    def visitReturn_stat(self, ctx: MT22Parser.Return_statContext):
        return ReturnStmt(ctx.expr().accept(self) if ctx.expr() else None)

    # call_stat : func_name LP expr_list? RP SEMI ;
    def visitCall_stat(self, ctx: MT22Parser.Call_statContext):
        name = ctx.func_name().accept(self)
        args = ctx.expr_list().accept(self) if ctx.expr_list() else []
        return CallStmt(name, args)

    # func_name: ID;
    def visitFunc_name(self, ctx: MT22Parser.Func_nameContext):
        return Id(ctx.ID().getText())

    # block_stat: LCB body_block_stat? RCB;
    def visitBlock_stat(self, ctx: MT22Parser.Block_statContext):
        body = ctx.body_block_stat().accept(self) if ctx.body_block_stat() else []
        return BlockStmt(body)

    # body_block_stat: (vardecl | stat) body_block_stat| (vardecl | stat);
    def visitBody_block_stat(self, ctx: MT22Parser.Body_block_statContext):
        result = []
        res = ctx.getChild(0).accept(self)
        if self.check_if_array(res):
            result.extend(res)
        else:
            result.append(res)
        if ctx.body_block_stat():
            result.extend(ctx.body_block_stat().accept(self))
        return result

    # expr_list_for_valdecl: expr COMMA expr_list_for_valdecl| expr;
    def visitExpr_list_for_valdecl(self, ctx: MT22Parser.Expr_list_for_valdeclContext):
        return [ctx.expr().accept(self), *ctx.expr_list_for_valdecl().accept(self)] if ctx.COMMA() else [ctx.expr().accept(self)]

    # expr_list: expr COMMA expr_list| expr;
    def visitExpr_list(self, ctx: MT22Parser.Expr_list_for_valdeclContext):
        return [ctx.expr().accept(self), *ctx.expr_list().accept(self)] if ctx.COMMA() else [ctx.expr().accept(self)]

    # expr : expr SCOPE_OP expr1| expr1;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.SCOPE_OP():
            op = ctx.SCOPE_OP().getText()
            left = ctx.expr1(0).accept(self)
            right = ctx.expr1(1).accept(self)
            return BinExpr(op, left, right)
        return ctx.expr1(0).accept(self)

    # expr1: expr2 (EQUAL | NOT_EQ | GREATER_THAN | LESS_THAN | GT_EQ | LT_EQ) expr2| expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = ctx.expr2(0).accept(self)
            right = ctx.expr2(1).accept(self)
            return BinExpr(op, left, right)
        return ctx.expr2(0).accept(self)

    # expr2: expr2 (AND | OR) expr3| expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = ctx.expr2().accept(self)
            right = ctx.expr3().accept(self)
            return BinExpr(op, left, right)
        return ctx.expr3().accept(self)

    # expr3: expr3 (ADD | MINUS) expr4| expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = ctx.expr3().accept(self)
            right = ctx.expr4().accept(self)
            return BinExpr(op, left, right)
        return ctx.expr4().accept(self)

    # expr4: expr4 (MUL | DIV | MOD) expr5| expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = ctx.expr4().accept(self)
            right = ctx.expr5().accept(self)
            return BinExpr(op, left, right)
        return ctx.expr5().accept(self)

    # expr5: NOT expr5| expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            val = ctx.expr5().accept(self)
            return UnExpr(op, val)
        return ctx.expr6().accept(self)

    # expr6: MINUS expr6| expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            val = ctx.expr6().accept(self)
            return UnExpr(op, val)
        return ctx.expr7().accept(self)

    # expr7: expr7 index_op| expr8;
    # # a[1, 2] -> ArrayCell(a, [1, 2])
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.getChildCount() == 2:
            cell = ctx.index_op().accept(self)
            name = ctx.expr7().accept(self)
            return ArrayCell(name, cell)
        return ctx.expr8().accept(self)

    # expr8: operands| LP expr RP;
    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        return ctx.expr().accept(self) if ctx.expr() else ctx.operands().accept(self)

    # func_call: func_name LP expr_list? RP;
    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        return FuncCall(ctx.func_name().accept(self), ctx.expr_list().accept(self) if ctx.expr_list() else [])

    # operands: (INT_LIT | FLOAT_LIT | BOOLEAN_LIT | STRING_LIT | array_lit)| func_call| ID;
    def visitOperands(self, ctx: MT22Parser.OperandsContext):
        if ctx.array_lit():
            return ctx.array_lit().accept(self)
        if ctx.func_call():
            return ctx.func_call().accept(self)
        if ctx.INT_LIT():
            return IntegerLit(ctx.getChild(0).getText())
        if ctx.FLOAT_LIT():
            return FloatLit(ctx.getChild(0).getText())
        if ctx.BOOLEAN_LIT():
            return BooleanLit(True if ctx.getChild(0).getText() == 'True' else False)
        if ctx.STRING_LIT():
            return StringLit(ctx.getChild(0).getText())
        return Id(ctx.getChild(0).getText())

    # index_op: LSB expr_list RSB;
    def visitIndex_op(self, ctx: MT22Parser.Index_opContext):
        return ctx.expr_list().accept(self)
