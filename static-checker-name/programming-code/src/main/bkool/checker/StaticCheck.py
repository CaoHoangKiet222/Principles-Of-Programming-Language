from Quiz4 import Quiz4Checker


class StaticChecker(Quiz4Checker):
    global_envi = []

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)
