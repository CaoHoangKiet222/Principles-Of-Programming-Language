from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):
    def visit(self, ast, param):
        return ast.accept(self, param)

    @abstractmethod
    def visitProgram(self, ast, param):
        pass

    @abstractmethod
    def visitVarDecl(self, ast, param):
        pass

    @abstractmethod
    def visitParamDecl(self, ast, param):
        pass

    @abstractmethod
    def visitFuncDecl(self, ast, param):
        pass

    @abstractmethod
    def visitIntegerType(self, ast, param):
        pass

    @abstractmethod
    def visitFloatType(self, ast, param):
        pass

    @abstractmethod
    def visitBooleanType(self, ast, param):
        pass

    @abstractmethod
    def visitStringType(self, ast, param):
        pass

    @abstractmethod
    def visitVoidType(self, ast, param):
        pass

    @abstractmethod
    def visitAutoType(self, ast, param):
        pass

    @abstractmethod
    def visitArrayType(self, ast, param):
        pass

    @abstractmethod
    def visitBinExpr(self, ast, param):
        pass

    @abstractmethod
    def visitUnExpr(self, ast, param):
        pass

    @abstractmethod
    def visitId(self, ast, param):
        pass

    @abstractmethod
    def visitArrayCell(self, ast, param):
        pass

    @abstractmethod
    def visitFuncCall(self, ast, param):
        pass

    @abstractmethod
    def visitBlockStmt(self, ast, param):
        pass

    @abstractmethod
    def visitIfStmt(self, ast, param):
        pass

    @abstractmethod
    def visitForStmt(self, ast, param):
        pass

    @abstractmethod
    def visitWhileStmt(self, ast, param):
        pass

    @abstractmethod
    def visitDoWhileStmt(self, ast, param):
        pass

    @abstractmethod
    def visitContinueStmt(self, ast, param):
        pass

    @abstractmethod
    def visitBreakStmt(self, ast, param):
        pass

    @abstractmethod
    def visitReturnStmt(self, ast, param):
        pass

    @abstractmethod
    def visitAssignStmt(self, ast, param):
        pass

    @abstractmethod
    def visitCallStmt(self, ast, param):
        pass

    @abstractmethod
    def visitIntegerLit(self, ast, param):
        pass

    @abstractmethod
    def visitFloatLit(self, ast, param):
        pass

    @abstractmethod
    def visitBooleanLit(self, ast, param):
        pass

    @abstractmethod
    def visitStringLit(self, ast, param):
        pass

    @abstractmethod
    def visitArrayLit(self, ast, param):
        pass


class BaseVisitor(Visitor):
    def visitProgram(self, ast, param):
        pass

    def visitVarDecl(self, ast, param):
        pass

    def visitParamDecl(self, ast, param):
        pass

    def visitFuncDecl(self, ast, param):
        pass

    def visitIntegerType(self, ast, param):
        pass

    def visitFloatType(self, ast, param):
        pass

    def visitBooleanType(self, ast, param):
        pass

    def visitStringType(self, ast, param):
        pass

    def visitVoidType(self, ast, param):
        pass

    def visitAutoType(self, ast, param):
        pass

    def visitArrayType(self, ast, param):
        pass

    def visitBinExpr(self, ast, param):
        pass

    def visitUnExpr(self, ast, param):
        pass

    def visitId(self, ast, param):
        pass

    def visitArrayCell(self, ast, param):
        pass

    def visitFuncCall(self, ast, param):
        pass

    def visitBlockStmt(self, ast, param):
        pass

    def visitIfStmt(self, ast, param):
        pass

    def visitForStmt(self, ast, param):
        pass

    def visitWhileStmt(self, ast, param):
        pass

    def visitDoWhileStmt(self, ast, param):
        pass

    def visitContinueStmt(self, ast, param):
        pass

    def visitBreakStmt(self, ast, param):
        pass

    def visitReturnStmt(self, ast, param):
        pass

    def visitAssignStmt(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

    def visitIntegerLit(self, ast, param):
        pass

    def visitFloatLit(self, ast, param):
        pass

    def visitBooleanLit(self, ast, param):
        pass

    def visitStringLit(self, ast, param):
        pass

    def visitArrayLit(self, ast, param):
        pass
