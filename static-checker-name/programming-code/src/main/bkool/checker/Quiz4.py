from AST import *
from Visitor import *
from StaticError import *


class Quiz4Checker(BaseVisitor):
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

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        o.append(ctx.name)

        list_decl = []
        for p in ctx.param:
            self.visit(p, list_decl)

        for element in ctx.body:
            for e in element:
                if type(e) in [VarDecl, ConstDecl]:
                    self.visit(e, list_decl)
                if type(e) in [FuncDecl]:
                    list_decl = list(set(o + list_decl))
                    self.visit(e, list_decl)
                if type(e) in [Id, IntLit]:
                    self.visit(e, list(set(o + list_decl)))

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass

    def visitId(self, ctx: Id, o: object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
