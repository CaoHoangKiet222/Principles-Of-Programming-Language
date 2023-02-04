import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # # # Test Variable Declarations # # #
    def test_1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl(Id("x"), IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(Id(x), IntegerType, IntegerLit(1))
	VarDecl(Id(y), IntegerType, IntegerLit(2))
	VarDecl(Id(z), IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_3(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(Id(x), IntegerType, IntegerLit(1))
	VarDecl(Id(y), IntegerType, IntegerLit(2))
	VarDecl(Id(z), IntegerType, IntegerLit(3))
	VarDecl(Id(a), FloatType)
	VarDecl(Id(b), FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b, c: auto = 1 , 2 , 3;
        d, e, f: string = "hello_d" , "hello_e", "hello_f" ;
        a, b, c: float = 2.000001, 3.0000001, 40_1.1;
        a, b, c: boolean = true, false, true;
"""
        expect = """Program([
	VarDecl(Id(x), IntegerType, IntegerLit(1))
	VarDecl(Id(y), IntegerType, IntegerLit(2))
	VarDecl(Id(z), IntegerType, IntegerLit(3))
	VarDecl(Id(a), AutoType, IntegerLit(1))
	VarDecl(Id(b), AutoType, IntegerLit(2))
	VarDecl(Id(c), AutoType, IntegerLit(3))
	VarDecl(Id(d), StringType, StringLit(hello_d))
	VarDecl(Id(e), StringType, StringLit(hello_e))
	VarDecl(Id(f), StringType, StringLit(hello_f))
	VarDecl(Id(a), FloatType, FloatLit(2.000001))
	VarDecl(Id(b), FloatType, FloatLit(3.0000001))
	VarDecl(Id(c), FloatType, FloatLit(401.1))
	VarDecl(Id(a), BooleanType, BooleanLit(False))
	VarDecl(Id(b), BooleanType, BooleanLit(False))
	VarDecl(Id(c), BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = """
    a, b, c: array [2, 3] of integer;
"""
        expect = """Program([
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

#     def test_simple_program(self):
#         """Simple program"""
#         input = """main: function void () {
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))
#
#     def test_more_complex_program(self):
#         """More complex program"""
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 305))
