import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # Quiz1
    def test_1(self):
        input = Program([VarDecl("a", IntType()), ConstDecl(
            "b", IntLit(3)), VarDecl("a", FloatType())])
        expect = "a"
        self.assertTrue(TestChecker.test(input, expect, 100))

    def test_2(self):
        input = Program([VarDecl("b", IntType()), ConstDecl(
            "b", IntLit(3)), VarDecl("a", FloatType())])
        expect = "b"
        self.assertTrue(TestChecker.test(input, expect, 101))

    def test_3(self):
        input = Program([VarDecl("a", IntType()), ConstDecl(
            "c", IntLit(3)), VarDecl("c", FloatType())])
        expect = "c"
        self.assertTrue(TestChecker.test(input, expect, 102))

    def test_4(self):
        input = Program([VarDecl("a", IntType()), ConstDecl(
            "b", IntLit(3)), VarDecl("c", FloatType())])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 103))
