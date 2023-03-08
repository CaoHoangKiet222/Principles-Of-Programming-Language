import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_1(self):
    #     input = Program([
    #         FuncDecl(Id("main"), [], VoidType(), Block([], [
    #             CallExpr(Id("putInt"), [IntLiteral(5)])]))])
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))

    # def test_2(self):
    #     input = Program([
    #         FuncDecl(Id("main"), [], VoidType(), Block([], [
    #             CallExpr(Id("putInt"), [BinExpr("+", IntLiteral(5), IntLiteral(3))])]))])
    #     expect = "8"
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))

    # def test_3(self):
    #     input = Program([
    #         FuncDecl(Id("main"), [], VoidType(), Block([], [
    #             CallExpr(Id("putInt"), [BinExpr("*", BinExpr("-", IntLiteral(5), IntLiteral(3)), IntLiteral(3))])]))])
    #     expect = "6"
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))

    # def test_4(self):
    #     input = Program([
    #         FuncDecl(Id("main"), [], VoidType(), Block([], [
    #             CallExpr(Id("putFloat"), [BinExpr("+.", FloatLiteral(-1.0), FloatLiteral(1.0))])]))])
    #     expect = "0.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))

    # def test_5(self):
    #     input = Program([
    #         FuncDecl(Id("main"), [], VoidType(), Block([], [
    #             CallExpr(Id("putFloat"), [BinExpr("*.", FloatLiteral(1.0), BinExpr("-.", FloatLiteral(10.0), FloatLiteral(2.0)))])]))])
    #     expect = "8.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    # def test_6(self):
    #     input = Program([
    #         FuncDecl(Id("main"), [], VoidType(), Block([], [
    #             CallExpr(Id("putInt"), [BinExpr("/", BinExpr("-", IntLiteral(5), IntLiteral(3)), IntLiteral(3))])]))])
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test_7(self):
    #     input = Program([VarDecl(Id("x"), IntType()), FuncDecl(Id("main"), [], VoidType(
    #     ), Block([VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), IntType()), VarDecl(Id("z"), FloatType())], []))])
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))

    # def test_8(self):
    #     input = Program([VarDecl(Id("x"), IntType()), FuncDecl(Id("main"), [], VoidType(), Block(
    #         [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), IntType())], [Block([VarDecl(Id("z"), FloatType())], []), Block([VarDecl(Id("t"), FloatType())], [])]))])
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))

    # def test_9(self):
    #     input = Program([VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), IntType()), FuncDecl(Id("main"), [], VoidType(), Block(
    #         [VarDecl(Id("a"), FloatType()), VarDecl(Id("b"), IntType()), VarDecl(Id("y"), IntType())], [Block([VarDecl(Id("z"), FloatType())], [Block([VarDecl(Id("z"), FloatType())], [])]), Block([VarDecl(Id("t"), FloatType())], [])]))])
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_10(self):
        input = Program([VarDecl(Id("x"), IntType()), FuncDecl(Id("main"), [], VoidType(), Block(
            [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), IntType()), VarDecl(Id("z"), FloatType())], []))])
        expect = """"""
        self.assertTrue(TestCodeGen.test(input, expect, 510))
