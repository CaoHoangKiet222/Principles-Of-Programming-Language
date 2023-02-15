import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # Quiz1
    # def test_1(self):
    #     input = Program([VarDecl("a", IntType()), ConstDecl(
    #         "b", IntLit(3)), VarDecl("a", FloatType())])
    #     expect = "a"
    #     self.assertTrue(TestChecker.test(input, expect, 100))

    # def test_2(self):
    #     input = Program([VarDecl("b", IntType()), ConstDecl(
    #         "b", IntLit(3)), VarDecl("a", FloatType())])
    #     expect = "b"
    #     self.assertTrue(TestChecker.test(input, expect, 101))

    # def test_3(self):
    #     input = Program([VarDecl("a", IntType()), ConstDecl(
    #         "c", IntLit(3)), VarDecl("c", FloatType())])
    #     expect = "c"
    #     self.assertTrue(TestChecker.test(input, expect, 102))

    # def test_4(self):
    #     input = Program([VarDecl("a", IntType()), ConstDecl(
    #         "b", IntLit(3)), VarDecl("c", FloatType())])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 103))

    # Quiz2
    # def test_5(self):
    #     input = Program([VarDecl("a", IntType()), ConstDecl(
    #         "b", IntLit(3)), VarDecl("a", FloatType())])
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 104))

    # def test_6(self):
    #     input = Program([VarDecl("b", IntType()), ConstDecl(
    #         "b", IntLit(3)), VarDecl("a", FloatType())])
    #     expect = "Redeclared Constant: b"
    #     self.assertTrue(TestChecker.test(input, expect, 105))

    # def test_7(self):
    #     input = Program([VarDecl("a", IntType()), ConstDecl(
    #         "c", IntLit(3)), VarDecl("c", FloatType())])
    #     expect = "Redeclared Variable: c"
    #     self.assertTrue(TestChecker.test(input, expect, 106))

    # def test_8(self):
    #     input = Program([VarDecl("a", IntType()), ConstDecl(
    #         "b", IntLit(3)), VarDecl("c", FloatType())])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 107))

    # Quiz3
    # def test_9(self):
    #     input = Program([VarDecl("a", IntType()), ConstDecl(
    #         "b", IntLit(3)), FuncDecl("a", [], [])])
    #     expect = "Redeclared Function: a"
    #     self.assertTrue(TestChecker.test(input, expect, 108))

    # def test_10(self):
    #     input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("a", FloatType())], [
    #                     ConstDecl("c", IntLit(3)), VarDecl("b", IntType()), VarDecl("c", IntType())])])
    #     expect = "Redeclared Variable: c"
    #     self.assertTrue(TestChecker.test(input, expect, 109))

    # def test_11(self):
    #     input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl(
    #         "b", IntType()), VarDecl("m", FloatType())], [ConstDecl("c", IntLit(3)), VarDecl("d", IntType())])])
    #     expect = "Redeclared Variable: m"
    #     self.assertTrue(TestChecker.test(input, expect, 110))

    # def test_12(self):
    #     input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl(
    #         "b", IntType()), VarDecl("d", FloatType())], [ConstDecl("c", IntLit(3)), VarDecl("d", IntType())])])
    #     expect = "Redeclared Variable: d"
    #     self.assertTrue(TestChecker.test(input, expect, 111))

    # def test_13(self):
    #     input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl(
    #         "b", IntType()), VarDecl("d", FloatType())], [ConstDecl("c", IntLit(3)), FuncDecl("d", [], [])])])
    #     expect = "Redeclared Function: d"
    #     self.assertTrue(TestChecker.test(input, expect, 112))

    # def test_14(self):
    #     input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl("b", IntType()), VarDecl(
    #         "d", FloatType())], [ConstDecl("c", IntLit(3)), FuncDecl("foo", [VarDecl("x", IntType())], [VarDecl("x", IntType())])])])
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 113))

    # Quiz4
    def test_15(self):
        input = Program([VarDecl("a", IntType()), ConstDecl(
            "b", IntLit(3)), FuncDecl("a", [], ([], []))])
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 114))

    def test_16(self):
        input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("a", FloatType())], ([
                        ConstDecl("c", IntLit(3)), VarDecl("b", IntType()), VarDecl("c", IntType())], []))])
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 115))

    def test_17(self):
        input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl(
            "b", IntType()), VarDecl("m", FloatType())], ([ConstDecl("c", IntLit(3)), VarDecl("d", IntType())], []))])
        expect = "Redeclared Variable: m"
        self.assertTrue(TestChecker.test(input, expect, 116))

    def test_18(self):
        input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl(
            "b", IntType()), VarDecl("d", FloatType())], ([ConstDecl("c", IntLit(3)), VarDecl("d", IntType())], []))])
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input, expect, 117))

    def test_19(self):
        input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl(
            "b", IntType()), VarDecl("d", FloatType())], ([ConstDecl("c", IntLit(3)), FuncDecl("d", [], ([], []))], []))])
        expect = "Redeclared Function: d"
        self.assertTrue(TestChecker.test(input, expect, 118))

    def test_20(self):
        input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl("b", IntType()), VarDecl(
            "d", FloatType())], ([ConstDecl("c", IntLit(3)), FuncDecl("foo", [VarDecl("x", IntType())], ([VarDecl("x", IntType())], []))], []))])
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 119))

    def test_21(self):
        input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl("b", IntType()), VarDecl("d", FloatType())], ([ConstDecl("c", IntLit(3)), FuncDecl(
            "foo", [VarDecl("x", IntType())], ([VarDecl("y", IntType()), VarDecl("z", IntType())], [Id("y"), Id("x"), Id("foo"), Id("c"), Id("m"), Id("a")]))], [Id("foo"), Id("d"), Id("z")]))])
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input, expect, 120))

    def test_22(self):
        input = Program([VarDecl("a", IntType()), ConstDecl("b", IntLit(3)), FuncDecl(
            "c", [], ([], [IntLit(1), Id("a"), Id("d"), Id("b")]))])
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 121))

    def test_23(self):
        input = Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl("b", IntType()), VarDecl("n", FloatType())], ([
                        ConstDecl("c", IntLit(3)), VarDecl("d", IntType())], [Id("a"), Id("b"), Id("c"), Id("d"), IntLit(3), Id("m"), Id("q"), Id("n")]))])
        expect = "Undeclared Identifier: q"
        self.assertTrue(TestChecker.test(input, expect, 122))

    def test_24(self):
        input = Program([VarDecl("t", IntType()), FuncDecl("a", [VarDecl("m", FloatType()), VarDecl("b", IntType()), VarDecl("d", FloatType())], ([ConstDecl("c", IntLit(3)), FuncDecl("foo", [VarDecl("x", IntType())], ([VarDecl("y", IntType()), VarDecl("z", IntType())], [Id("y"), Id("x"), Id("foo"), Id("c"), Id("m"), Id("a"), Id("t")])),
                                                                                                                                                  FuncDecl("foo1", [], ([], [Id("foo"), Id("d"), Id("x")]))], [Id("foo"), Id("d"), Id("foo1")]))])
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 123))
