import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test_1(self):
    #     input = """
    #     x: integer = 65;
    #     fact: function integer (n: integer) {
    #         if (n == 0) return 1;
    #         else return n * fact(n - 1);
    #     }
    #     inc: function void(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = fact(3);
    #         inc(x, delta);
    #         printInteger(x);
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_1(self):
    #     input = """
    #     a: float;
    #     x: integer = a + 2;
    #     """
    #     expect = "Type Mismatch In Expression: VarDecl(Id(x), IntegerType, BinExpr(+, Id(a), IntegerLit(2)))"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_2(self):
    #     input = """
    #     c: integer = 2.3;
    #     """
    #     expect = "Type Mismatch In Expression: VarDecl(Id(c), IntegerType, FloatLit(2.3))"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_3(self):
    #     input = """
    #     c: float = 2.3;
    #     c: string;
    #     """
    #     expect = "Redeclared Variable: c"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_4(self):
    #     input = """
    #     a: auto = 10;
    #     c: auto = !(a < 100);
    #     d: auto = c;
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test_5(self):
    #     input = """
    #     b: auto = "hello";
    #     c: auto = b == "hello1";
    #     """
    #     expect = "Type Mismatch In Expression: BinExpr(==, Id(b), StringLit(hello1))"
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_6(self):
    #     input = """
    #     b: auto = true;
    #     c: auto = b == false;
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # # Not update assignment yet
    # def test_7(self):
    #     input = """
    #     b: auto = 1 == true;
    #     c: auto = b == false;
    #     """
    #     expect = "Type Mismatch In Expression: BinExpr(==, IntegerLit(1), BooleanLit(False))"
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_8(self):
    #     input = """
    #     x: integer = 9_9999_999;
    #     y: integer = x == 1;
    #     """
    #     expect = "Type Mismatch In Expression: VarDecl(Id(y), IntegerType, BinExpr(==, Id(x), IntegerLit(1)))"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test_9(self):
    #     input = """
    #     a: array [2] of integer = {1, 2};
    #     b: array [2, 3] of integer = {{}, {}};
    #     c: array [2, 3] of integer = {{1}, {1, 2, 3}};
    #     d: array [2, 3, 5] of integer = {{{1, 3, 4}, {5, 6}, {}}, {{1}, {2}, {1}}};
    #     e: array [2, 3] of integer = {{1.0}, {1, 2, 3}};
    #     f: array [2, 3] of integer = {{1, 1}, {1.0, 2, 3}};
    #     """
    #     expect = "Illegal Array Literal: ArrayLit([FloatLit(1.0), IntegerLit(2), IntegerLit(3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    # def test_10(self):
    #     input = """
    #     x, y, z: integer = 1, 2, 3;
    #     a: array [3, 2] of integer = {{x + z}, {y, z}};
    #     b: array [2, 3] of integer = {1, {1, 3, 4}};
    #     """
    #     expect = "Illegal Array Literal: ArrayLit([IntegerLit(1), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4)])])"
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    # def test_11(self):
    #     input = """
    #     a: array [2, 3] of float = {{1}, {1, 3, 4}};
    #     b: array [2, 3] of integer = {{1.0}, {1.0, 3.0, 4.0}};
    #     """
    #     expect = "Type Mismatch In Expression: VarDecl(Id(b), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([FloatLit(1.0), FloatLit(3.0), FloatLit(4.0)])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    # def test_12(self):
    #     input = """
    #     a: array [2, 3] of float = {{1}, {1, 3, 4}};
    #     b: array [2, 3] of integer = {{1.0}, {1.0, 3.0, 4.0}};
    #     """
    #     expect = "Type Mismatch In Expression: VarDecl(Id(b), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([FloatLit(1.0), FloatLit(3.0), FloatLit(4.0)])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """
        // a: array [2, 3] of integer = {{1}, {1, 3, 4}};
        // a: array [2, 3] of integer = {{}};
        // a: array [2, 3] of integer = {{}, {}, {}};
        // a: array [2, 3] of integer = {{1}, {1, 3, 4, 5}};
        // b: array [2, 3, 2] of integer = {{{1, 3, 4}, {5, 6}, {}}, {{1}, {2}, {1}}};
        // a: array [2, 3] of boolean = {{1}, {false}};
        // a: array [2, 3] of boolean = {{false, false}, {1}};
        // a: array [2, 3] of boolean = {};
        b: array [2, 3] of boolean = {1};
        // c: array [2, 3] of boolean = {{}};
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 413))
