import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # Quiz1
    def test_1(self):
        input = BinOp("+", IntLit(3), BoolLit(True))
        expect = """Type Mismatch In Expression: BinOp("+",IntLit(3),BoolLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 100))

    def test_2(self):
        input = BinOp("*", BinOp("+", IntLit(3), FloatLit(3.4)),
                      BinOp(">", IntLit(3), FloatLit(2.1)))
        expect = """Type Mismatch In Expression: BinOp(">",IntLit(3),FloatLit(2.1))"""
        self.assertTrue(TestChecker.test(input, expect, 101))

    def test_3(self):
        input = BinOp("&&", BinOp(">", BinOp("-", IntLit(3), FloatLit(3.4)),
                      UnOp("-", FloatLit(2.1))), UnOp("-", BoolLit(True)))
        expect = """Type Mismatch In Expression: UnOp("-",BoolLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 102))

    def test_4(self):
        input = UnOp("-", BinOp(">", BinOp("-", IntLit(3),
                     FloatLit(3.4)), UnOp("-", FloatLit(2.1))))
        expect = """Type Mismatch In Expression: UnOp("-",BinOp(">",BinOp("-",IntLit(3),FloatLit(3.4)),UnOp("-",FloatLit(2.1))))"""
        self.assertTrue(TestChecker.test(input, expect, 103))

    def test_5(self):
        input = BinOp(">", BinOp("&&", BoolLit(True), BoolLit(False)), BinOp(
            "||", BoolLit(True), UnOp("-", FloatLit(2.3))))
        expect = """Type Mismatch In Expression: BinOp("||",BoolLit(True),UnOp("-",FloatLit(2.3)))"""
        self.assertTrue(TestChecker.test(input, expect, 104))

    def test_6(self):
        input = UnOp("!", BinOp("==", IntLit(
            3), BinOp("*", IntLit(5), IntLit(7))))
        expect = "BoolType"
        self.assertTrue(TestChecker.test(input, expect, 105))

    def test_7(self):
        input = UnOp("!", BinOp("==", IntLit(
            3), BinOp("/", IntLit(5), IntLit(7))))
        expect = """Type Mismatch In Expression: BinOp("==",IntLit(3),BinOp("/",IntLit(5),IntLit(7)))"""
        self.assertTrue(TestChecker.test(input, expect, 106))

    def test_8(self):
        input = UnOp("!", BinOp("-", IntLit(3),
                     BinOp("/", IntLit(5), IntLit(7))))
        expect = """Type Mismatch In Expression: UnOp("!",BinOp("-",IntLit(3),BinOp("/",IntLit(5),IntLit(7))))"""
        self.assertTrue(TestChecker.test(input, expect, 107))

    def test_9(self):
        input = BinOp("/", IntLit(8), BinOp("<", IntLit(3), IntLit(8)))
        expect = """Type Mismatch In Expression: BinOp("/",IntLit(8),BinOp("<",IntLit(3),IntLit(8)))"""
        self.assertTrue(TestChecker.test(input, expect, 108))

    def test_10(self):
        input = BinOp("||", BoolLit(True), BinOp("<", IntLit(3), IntLit(8)))
        expect = "BoolType"
        self.assertTrue(TestChecker.test(input, expect, 109))

    # Quiz2
    # def test_11(self):
    #     input = Program([VarDecl("x", IntType())], BinOp(
    #         "*", BinOp("+", Id("x"), FloatLit(3.4)), BinOp(">", IntLit(3), FloatLit(2.1))))
    #     expect = """Type Mismatch In Expression: BinOp(">",IntLit(3),FloatLit(2.1))"""
    #     self.assertTrue(TestChecker.test(input, expect, 110))

    # def test_12(self):
    #     input = Program([], BinOp("+", IntLit(3), BoolLit(True)))
    #     expect = """Type Mismatch In Expression: BinOp("+",IntLit(3),BoolLit(True))"""
    #     self.assertTrue(TestChecker.test(input, expect, 111))

    # def test_13(self):
    #     input = Program([VarDecl("x", IntType()), VarDecl("y", BoolType())], BinOp("&&", BinOp(
    #         ">", BinOp("-", IntLit(3), FloatLit(3.4)), UnOp("-", FloatLit(2.1))), UnOp("-", Id("y"))))
    #     expect = """Type Mismatch In Expression: UnOp("-",Id("y"))"""
    #     self.assertTrue(TestChecker.test(input, expect, 112))

    # def test_14(self):
    #     input = Program([VarDecl("x", IntType())], UnOp(
    #         "-", BinOp(">", BinOp("-", Id("x"), FloatLit(3.4)), UnOp("-", FloatLit(2.1)))))
    #     expect = """Type Mismatch In Expression: UnOp("-",BinOp(">",BinOp("-",Id("x"),FloatLit(3.4)),UnOp("-",FloatLit(2.1))))"""
    #     self.assertTrue(TestChecker.test(input, expect, 113))

    # def test_15(self):
    #     input = Program([VarDecl("x", BoolType()), VarDecl("y", BoolType()), VarDecl("z", FloatType())], BinOp(
    #         ">", BinOp("&&", Id("x"), Id("y")), BinOp("||", BoolLit(True), UnOp("-", Id("z")))))
    #     expect = """Type Mismatch In Expression: BinOp("||",BoolLit(True),UnOp("-",Id("z")))"""
    #     self.assertTrue(TestChecker.test(input, expect, 114))

    # def test_16(self):
    #     input = Program([VarDecl("x", IntType()), VarDecl("y", IntType()), VarDecl(
    #         "z", IntType())], UnOp("!", BinOp("==", Id("z"), BinOp("*", Id("y"), Id("x")))))
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 115))

    # def test_17(self):
    #     input = Program([VarDecl("x", IntType()), VarDecl("y", IntType()), VarDecl(
    #         "z", IntType())], UnOp("!", BinOp("==", Id("x"), BinOp("/", Id("y"), Id("z")))))
    #     expect = """Type Mismatch In Expression: BinOp("==",Id("x"),BinOp("/",Id("y"),Id("z")))"""
    #     self.assertTrue(TestChecker.test(input, expect, 116))

    # def test_18(self):
    #     input = Program([VarDecl("x", IntType()), VarDecl("y", IntType()), VarDecl(
    #         "z", IntType())], UnOp("!", BinOp("-", Id("z"), BinOp("/", Id("y"), Id("x")))))
    #     expect = """Type Mismatch In Expression: UnOp("!",BinOp("-",Id("z"),BinOp("/",Id("y"),Id("x"))))"""
    #     self.assertTrue(TestChecker.test(input, expect, 117))

    # def test_19(self):
    #     input = Program([VarDecl("x", IntType()), VarDecl("y", IntType()), VarDecl(
    #         "z", IntType())], BinOp("/", Id("x"), BinOp("<", Id("y"), Id("z"))))
    #     expect = """Type Mismatch In Expression: BinOp("/",Id("x"),BinOp("<",Id("y"),Id("z")))"""
    #     self.assertTrue(TestChecker.test(input, expect, 118))

    # def test_20(self):
    #     input = Program([VarDecl("x", IntType()), VarDecl("y", IntType()), VarDecl(
    #         "z", IntType())], BinOp("||", BoolLit(True), BinOp("<", IntLit(3), Id("t"))))
    #     expect = "Undeclared Identifier: t"
    #     self.assertTrue(TestChecker.test(input, expect, 119))
