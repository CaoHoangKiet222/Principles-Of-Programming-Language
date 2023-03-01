import unittest
from TestUtils import TestAST


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """int a;"""
        expect = "Program([VarDecl(Id(a),IntType)])"
        self.assertTrue(TestAST.test(input, expect, 100))

    def test_2(self):
        input = """int a,b;"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)])"
        self.assertTrue(TestAST.test(input, expect, 101))

    def test_3(self):
        input = "int a;float b;"
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType)])"
        self.assertTrue(TestAST.test(input, expect, 102))

    def test_4(self):
        input = "int a,b;float c;"
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType)])"
        self.assertTrue(TestAST.test(input, expect, 103))
