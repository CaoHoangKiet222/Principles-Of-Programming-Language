from Quiz5 import Quiz5Checker


class StaticChecker(Quiz5Checker):
    global_envi = []

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)
