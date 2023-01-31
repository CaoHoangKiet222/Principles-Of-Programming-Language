class Exp:
    def __init__(self, operator: str) -> None:
        self.operator = operator


class BinExp(Exp):
    def __init__(self, op1, operator, op2) -> None:
        self.op1 = op1
        self.op2 = op2
        super().__init__(operator)

    def eval(self):
        match self.operator:
            case '+':
                return self.op1.eval() + self.op2.eval()
            case '-':
                return self.op1.eval() - self.op2.eval()
            case '*':
                return self.op1.eval() * self.op2.eval()
            case '/':
                return self.op1.eval() / self.op2.eval()

    def printPrefix(self):
        return self.operator + ' ' + self.op1.printPrefix() + ' ' + self.op2.printPrefix()


class UnExp(Exp):
    def __init__(self, operator, op) -> None:
        self.op = op
        super().__init__(operator)

    def eval(self):
        match self.operator:
            case '+':
                return self.op.eval()
            case '-':
                return -self.op.eval()

    def printPrefix(self):
        return self.operator + '. ' + self.op.printPrefix()


class IntLit(Exp):
    def __init__(self, number) -> None:
        self.int_number = number

    def eval(self):
        return self.int_number

    def printPrefix(self):
        return str(self.int_number)


class FloatLit(Exp):
    def __init__(self, number) -> None:
        self.float_number = number

    def eval(self):
        return self.float_number

    def printPrefix(self):
        return str(self.float_number)


x1 = IntLit(1)

x2 = FloatLit(2.0)

x3 = BinExp(x1, "+", x1)

x4 = UnExp("-", x1)

x5 = BinExp(x4, "+", BinExp(IntLit(4), "*", x2))
print(x1.eval())
print(x2.eval())
print(x3.eval())
print(x4.eval())
print(x5.eval())
print(x1.printPrefix())
print(x2.printPrefix())
print(x3.printPrefix())
print(x4.printPrefix())
print(x5.printPrefix())
