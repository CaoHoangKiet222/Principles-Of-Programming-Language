import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # Quiz3
    # def test_1(self):
    #     input = Program([VarDecl("x")], [Assign(Id("x"), BinOp(
    #         "*", BinOp("+", Id("x"), IntLit(3.4)), BinOp("-", Id("x"), FloatLit(2.1))))])
    #     expect = """Type Mismatch In Expression: BinOp("-",Id("x"),FloatLit(2.1))"""
    #     self.assertTrue(TestChecker.test(input, expect, 100))

    # def test_2(self):
    #     input = Program([VarDecl("x"), VarDecl("y"), VarDecl("z")], [Assign(Id("x"), BinOp(">b", BinOp("&&", Id(
    #         "x"), Id("y")), BinOp("||", BoolLit(False), BinOp(">", Id("z"), IntLit(3))))), Assign(Id("z"), Id("x"))])
    #     expect = """Type Mismatch In Statement: Assign(Id("z"),Id("x"))"""
    #     self.assertTrue(TestChecker.test(input, expect, 101))

    # def test_3(self):
    #     input = Program([VarDecl("x"), VarDecl("y")],
    #                     [Assign(Id("x"), Id("y"))])
    #     expect = """Type Cannot Be Inferred: Assign(Id("x"),Id("y"))"""
    #     self.assertTrue(TestChecker.test(input, expect, 102))

    # def test_4(self):
    #     input = Program([VarDecl("x"), VarDecl("y"), VarDecl("z")], [Assign(Id("z"), BinOp(
    #         "&&", BinOp(">", BinOp("-", Id("x"), IntLit(3)), UnOp("-", Id("y"))), UnOp("!", Id("y"))))])
    #     expect = """Type Mismatch In Expression: UnOp("!",Id("y"))"""
    #     self.assertTrue(TestChecker.test(input, expect, 103))

    # def test_5(self):
    #     input = Program([VarDecl("x")], [Assign(Id("x"), UnOp(
    #         "-", BinOp(">.", BinOp("-.", Id("x"), FloatLit(3.4)), UnOp("-.", FloatLit(2.1)))))])
    #     expect = """Type Mismatch In Expression: UnOp("-",BinOp(">.",BinOp("-.",Id("x"),FloatLit(3.4)),UnOp("-.",FloatLit(2.1))))"""
    #     self.assertTrue(TestChecker.test(input, expect, 104))

    # def test_6(self):
    #     input = Program([VarDecl("x"), VarDecl("y"), VarDecl("z")], [Assign(
    #         Id("x"), UnOp("!", BinOp("=", Id("z"), BinOp("*", Id("y"), Id("x")))))])
    #     expect = """Type Mismatch In Statement: Assign(Id("x"),UnOp("!",BinOp("=",Id("z"),BinOp("*",Id("y"),Id("x")))))"""
    #     self.assertTrue(TestChecker.test(input, expect, 105))

    # def test_7(self):
    #     input = Program([VarDecl("x"), VarDecl("y"), VarDecl("z")], [Assign(Id("x"), UnOp(
    #         "-.", BinOp("-.", Id("z"), BinOp("/.", UnOp("i2f", Id("y")), Id("x"))))), Assign(Id("y"), FloatLit(3.2))])
    #     expect = """Type Mismatch In Statement: Assign(Id("y"),FloatLit(3.2))"""
    #     self.assertTrue(TestChecker.test(input, expect, 106))

    # Quiz4
    def test_8(self):
        input = Program([VarDecl("x")], [Assign(Id("x"), IntLit(3)), Block([VarDecl("y"), VarDecl(
            "x"), VarDecl("y")], [Assign(Id("x"), Id("y")), Assign(Id("y"), IntLit(3))])])
        expect = """Redeclared: VarDecl("y")"""
        self.assertTrue(TestChecker.test(input, expect, 107))

    def test_9(self):
        input = Program([VarDecl("x")], [Assign(Id("x"), IntLit(3)), Block(
            [VarDecl("y")], [Assign(Id("x"), Id("y")), Assign(Id("y"), BoolLit(True))])])
        expect = """Type Mismatch In Statement: Assign(Id("y"),BoolLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 108))

    def test_10(self):
        input = Program([VarDecl("x")], [Assign(Id("x"), IntLit(3)), Block([VarDecl(
            "y"), VarDecl("x")], [Assign(Id("x"), Id("y")), Assign(Id("y"), FloatLit(3))])])
        expect = """Type Cannot Be Inferred: Assign(Id("x"),Id("y"))"""
        self.assertTrue(TestChecker.test(input, expect, 109))

    def test_11(self):
        input = Program([VarDecl("x"), VarDecl("t")], [Assign(Id("x"), IntLit(3)), Block([VarDecl("y")], [
                        Assign(Id("x"), Id("y")), Block([], [Assign(Id("t"), FloatLit(3)), Assign(Id("z"), Id("t"))])])])
        expect = """Undeclared Identifier: z"""
        self.assertTrue(TestChecker.test(input, expect, 110))

    def test_12(self):
        input = Program([VarDecl("x"), VarDecl("t")], [Assign(Id("x"), IntLit(3)), Block([VarDecl("y")], [Assign(
            Id("x"), Id("y")), Block([VarDecl("z")], [Assign(Id("t"), FloatLit(3)), Assign(Id("z"), UnOp("-", Id("t")))])])])
        expect = """Type Mismatch In Expression: UnOp("-",Id("t"))"""
        self.assertTrue(TestChecker.test(input, expect, 111))

    def test_13(self):
        input = Program([VarDecl("x"), VarDecl("t")], [Assign(Id("x"), IntLit(3)), Block([VarDecl("y")], [Assign(Id("x"), Id(
            "y")), Block([VarDecl("z")], [Assign(Id("t"), FloatLit(3)), Assign(Id("z"), BinOp("-", Id("t"), Id("x")))])])])
        expect = """Type Mismatch In Expression: BinOp("-",Id("t"),Id("x"))"""
        self.assertTrue(TestChecker.test(input, expect, 112))

    def test_14(self):
        input = Program([VarDecl("x"), VarDecl("t")], [Assign(Id("x"), IntLit(3)), Block([VarDecl("y")], [Assign(Id("x"), Id(
            "y")), Block([VarDecl("z")], [Assign(Id("t"), FloatLit(3)), Assign(Id("y"), BinOp("-.", Id("t"), UnOp("i2f", Id("x"))))])])])
        expect = """Type Mismatch In Statement: Assign(Id("y"),BinOp("-.",Id("t"),UnOp("i2f",Id("x"))))"""
        self.assertTrue(TestChecker.test(input, expect, 113))

    def test_15(self):
        input = Program([VarDecl("x"), VarDecl("t")], [Assign(Id("x"), IntLit(3)), Block([VarDecl("y")], [Assign(
            Id("x"), Id("y")), Block([VarDecl("z")], [Assign(Id("t"), FloatLit(3)), Assign(Id("z"), UnOp("floor", Id("y")))])])])
        expect = """Type Mismatch In Expression: UnOp("floor",Id("y"))"""
        self.assertTrue(TestChecker.test(input, expect, 114))

    def test_16(self):
        input = Program([VarDecl("x"), VarDecl("t")], [Assign(Id("x"), IntLit(3)), Block([VarDecl("x")], [
                        Assign(Id("x"), FloatLit(3.0)), Assign(Id("t"), Id("x"))]), Assign(Id("x"), Id("t"))])
        expect = """Type Mismatch In Statement: Assign(Id("x"),Id("t"))"""
        self.assertTrue(TestChecker.test(input, expect, 115))

    def test_17(self):
        input = Program([VarDecl("x")], [Assign(Id("x"), IntLit(3)), Block(
            [VarDecl("x")], [Assign(Id("x"), FloatLit(3.0))]), Assign(Id("x"), BoolLit(False))])
        expect = """Type Mismatch In Statement: Assign(Id("x"),BoolLit(False))"""
        self.assertTrue(TestChecker.test(input, expect, 116))

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
