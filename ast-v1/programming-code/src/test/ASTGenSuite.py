import unittest
from TestUtils import TestAST


class ASTGenSuite(unittest.TestCase):
    # quiz1: Count the terminal nodes in the parse tree
    # def test_1(self):
    #     input = """int a;"""
    #     expect = "4"
    #     self.assertTrue(TestAST.test(input, expect, 100))
    #
    # def test_2(self):
    #     input = """int a;int b;"""
    #     expect = "7"
    #     self.assertTrue(TestAST.test(input, expect, 101))
    #
    # def test_3(self):
    #     input = """int a;int b;float x, y, z;"""
    #     expect = "14"
    #     self.assertTrue(TestAST.test(input, expect, 102))

    # quiz2: Count the non-terminal nodes in the parse tree
    # def test_4(self):
    #     input = """int a;"""
    #     expect = "6"
    #     self.assertTrue(TestAST.test(input, expect, 103))
    #
    # def test_5(self):
    #     input = """int a;int b;"""
    #     expect = "10"
    #     self.assertTrue(TestAST.test(input, expect, 104))
    #
    # def test_6(self):
    #     input = """int a;int b;float x, y, z;"""
    #     expect = "16"
    #     self.assertTrue(TestAST.test(input, expect, 105))

    # quiz3: Generate the AST of a MP input
    def test_7(self):
        input = """int a;"""
        expect = "Program([VarDecl(Id(a),IntType)])"
        self.assertTrue(TestAST.test(input, expect, 106))

    def test_8(self):
        input = """int a,b;"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)])"
        self.assertTrue(TestAST.test(input, expect, 107))

    def test_9(self):
        input = "int a;float b;"
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType)])"
        self.assertTrue(TestAST.test(input, expect, 108))

    def test_10(self):
        input = "int a,b;float c;"
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType)])"
        self.assertTrue(TestAST.test(input, expect, 109))

    def test_11(self):
        input = "int a,b;float c,d,e;"
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType),VarDecl(Id(d),FloatType),VarDecl(Id(e),FloatType)])"
        self.assertTrue(TestAST.test(input, expect, 110))
