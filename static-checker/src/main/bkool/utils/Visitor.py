from abc import ABC, abstractmethod


class Visitor(ABC):

    def visit(self, ast, param):
        return ast.accept(self, param)

    @abstractmethod
    def visitProgram(self, ast, param):
        pass

    @abstractmethod
    def visitFuncDecl(self, ast, param):
        pass

    @abstractmethod
    def visitVarDecl(self, ast, param):
        pass

    @abstractmethod
    def visitConstDecl(self, ast, param):
        pass

    @abstractmethod
    def visitIntType(self, ast, param):
        pass

    @abstractmethod
    def visitFloatType(self, ast, param):
        pass

    @abstractmethod
    def visitId(self, ast, param):
        pass

    @abstractmethod
    def visitIntLit(self, ast, param):
        pass


class BaseVisitor(Visitor):

    def visitProgram(self, ast, param):
        return None

    def visitFuncDecl(self, ast, param):
        return None

    def visitConstDecl(self, ast, param):
        return None

    def visitVarDecl(self, ast, param):
        return None

    def visitIntType(self, ast, param):
        return None

    def visitFloatType(self, ast, param):
        return None

    def visitId(self, ast, param):
        return None

    def visitIntLit(self, ast, param):
        return None
