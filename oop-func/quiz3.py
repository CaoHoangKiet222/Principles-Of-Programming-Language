# Use visitor design pattern
from abc import ABC


class Exp(ABC):
    pass


class Eval:
    def visit(self, ctx):
        return ctx.accept(self)

    def visitBinExp(self, ctx):
        match ctx.op:
            case '+':
                return self.visit(ctx.left) + self.visit(ctx.right)
            case '-':
                return self.visit(ctx.left) - self.visit(ctx.right)
            case '*':
                return self.visit(ctx.left) * self.visit(ctx.right)
            case '/':
                return self.visit(ctx.left) / self.visit(ctx.right)

    def visitUnExp(self, ctx):
        match ctx.op:
            case '+':
                return self.visit(ctx.operand)
            case '-':
                return -self.visit(ctx.operand)

    def visitIntLit(self, ctx):
        return ctx.value

    def visitFloatLit(self, ctx):
        return ctx.value


class PrintPrefix:
    def visit(self, ctx):
        return ctx.accept(self)

    def visitBinExp(self, ctx):
        return ctx.op + ' ' + self.visit(ctx.left) + ' ' + self.visit(ctx.right)

    def visitUnExp(self, ctx):
        return ctx.op + '. ' + self.visit(ctx.operand)

    def visitIntLit(self, ctx):
        return str(ctx.value)

    def visitFloatLit(self, ctx):
        return str(ctx.value)


class PostPrefix:
    def visit(self, ctx):
        return ctx.accept(self)

    def visitBinExp(self, ctx):
        return self.visit(ctx.left) + ' ' + self.visit(ctx.right) + ' ' + ctx.op

    def visitUnExp(self, ctx):
        return self.visit(ctx.operand) + ' ' + ctx.op + '.'

    def visitIntLit(self, ctx):
        return str(ctx.value)

    def visitFloatLit(self, ctx):
        return str(ctx.value)


class BinExp(Exp):
    def __init__(self, o1, op, o2):
        self.left = o1
        self.op = op
        self.right = o2

    def accept(self, v):
        return v.visitBinExp(self)


class UnExp(Exp):
    def __init__(self, op, o1):
        self.op = op
        self.operand = o1

    def accept(self, v):
        return v.visitUnExp(self)


class IntLit(Exp):
    def __init__(self, v):
        self.value = v

    def accept(self, v):
        return v.visitIntLit(self)


class FloatLit(Exp):
    def __init__(self, v):
        self.value = v

    def accept(self, v):
        return v.visitFloatLit(self)


x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1, "+", x1)
x4 = UnExp("-", x1)
x5 = BinExp(x4, "+", BinExp(IntLit(4), "*", x2))
v1 = Eval()
v2 = PrintPrefix()
v3 = PostPrefix()

print(v1.visit(x1))
print(v2.visit(x1))
print(v3.visit(x1))
print(v1.visit(x2))
print(v2.visit(x2))
print(v3.visit(x2))
print(v1.visit(x3))
print(v2.visit(x3))
print(v3.visit(x3))
print(v1.visit(x4))
print(v2.visit(x4))
print(v3.visit(x4))
print(v1.visit(x5))
print(v2.visit(x5))
print(v3.visit(x5))
