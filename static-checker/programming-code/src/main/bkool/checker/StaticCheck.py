from Quiz1 import Quiz1Checker


class StaticChecker(Quiz1Checker):
    global_envi = []

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)
