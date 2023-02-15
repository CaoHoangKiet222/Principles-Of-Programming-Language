from AST import *
from Visitor import *
from StaticError import *


class Quiz2Checker(BaseVisitor):
    def visitProgram(self, ast, o):
        o = []
        for decl in ast.decl:
            self.visit(decl, o)
        return ""

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        o.append(ctx.name)

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        o.append(ctx.name)

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass
