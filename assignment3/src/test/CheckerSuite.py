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

    # # Test VarDecl
    # def test_1(self):
    #     input = """
    #     a: float;
    #     x: integer = a + 2;
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(x), IntegerType, BinExpr(+, Id(a), IntegerLit(2)))"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_2(self):
    #     input = """
    #     c: integer = 2.3;
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(c), IntegerType, FloatLit(2.3))"
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
    #     c: auto = c;
    #     """
    #     expect = "Redeclared Variable: c"
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
    #     c: auto;
    #     """
    #     expect = "Invalid Variable: c"
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
    #     expect = "Type Mismatch In Statement: VarDecl(Id(y), IntegerType, BinExpr(==, Id(x), IntegerLit(1)))"
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
    #     expect = "Type Mismatch In Statement: VarDecl(Id(e), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"
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
    #     expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([FloatLit(1.0), FloatLit(3.0), FloatLit(4.0)])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    # def test_12(self):
    #     input = """
    #     a: array [2, 3] of integer = {{1}, {1, 3, 4}};
    #     b: array [2, 3] of integer = {{}};
    #     c: array [2, 3] of integer = {{}, {}, {}};
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(c), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    # def test_13(self):
    #     input = """
    #     a: array [2, 3] of integer = {{1}, {1, 3, 4, 5}};
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4), IntegerLit(5)])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 413))

    # def test_14(self):
    #     input = """
    #     a: array [2, 3, 2] of integer = {{{}, {}, {}, {}}, {{}, {}, {}}};
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2, 3, 2], IntegerType), ArrayLit([ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([])]), ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([])])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 414))

    # def test_15(self):
    #     input = """
    #     a: array [2, 3] of boolean = {};
    #     b: array [2, 3] of boolean = {{}};
    #     c: array [2, 3] of boolean = {{true}, {false}};
    #     d: array [2, 3] of boolean = {{false, false}, {1}};
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(d), ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([BooleanLit(False), BooleanLit(False)]), ArrayLit([IntegerLit(1)])]))"
    #     self.assertTrue(TestChecker.test(input, expect, 415))

    # def test_16(self):
    #     input = """
    #     e: array [2, 3] of boolean = {false, true, true}; // -> dont know ask teacher
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(e), ArrayType([2, 3], BooleanType), ArrayLit([BooleanLit(False), BooleanLit(False), BooleanLit(False)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 416))

    # def test_17(self):
    #     input = """
    #     a: array[3] of integer = {1};
    #     b: integer = a[0] + 2;
    #     b: integer = -a[0, 1] + 2;
    #     """
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input, expect, 417))

    # # Test Function Declare
    # def test_18(self):
    #     input = """
    #     main: function void() {}
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 418))

    # def test_19(self):
    #     input = """
    #     inc: function void(out n: integer, delta: integer) {}
    #     main: function void() {}
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 419))

    # def test_20(self):
    #     input = """
    #     inc: function void(delta: integer, delta: float) {}
    #     main: function void() {}
    #     """
    #     expect = "Redeclared Parameter: delta"
    #     self.assertTrue(TestChecker.test(input, expect, 420))

    # def test_21(self):
    #     input = """
    #     inc: function void() {}
    #     inc: function void(out n: integer, delta: float) {}
    #     main: function void() {}
    #     """
    #     expect = "Redeclared Function: inc"
    #     self.assertTrue(TestChecker.test(input, expect, 421))

    # def test_22(self):
    #     input = """
    #     inc: function void(out n: integer, delta: float) {}
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 422))

    # def test_23(self):
    #     input = """
    #     inc: function void(out n: integer, delta: integer) {
    #         x, y, z: integer;
    #         a: auto = x;
    #     }
    #     main: function void() {}
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 423))

    # def test_24(self):
    #     input = """
    #     inc: function void(out n: integer, delta: integer) {
    #         a: auto;
    #     }
    #     main: function void() {}
    #     """
    #     expect = "Invalid Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    # def test_25(self):
    #     input = """
    #     inc: function void(out n: integer, delta: integer) {
    #         x, y, z: integer;
    #         a, b, c: boolean;
    #         n: integer;
    #     }
    #     main: function void() {}
    #     """
    #     expect = "Redeclared Variable: n"
    #     self.assertTrue(TestChecker.test(input, expect, 425))

    # def test_26(self):
    #     input = """
    #     inc: function void(out n: integer, delta: integer) {
    #         x, y, z: integer;
    #         a, b, c: boolean;
    #         n: integer;
    #     }
    #     main: function void() {}
    #     """
    #     expect = "Redeclared Variable: n"
    #     self.assertTrue(TestChecker.test(input, expect, 426))

    # Test IfStmt in Function
    # def test_27(self):
    #     input = """
    #     inc: function void(out n: integer, delta: integer) {
    #         if (n > delta) {
    #         } else {}
    #     }
    #     main: function void() {}
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 427))

    # def test_28(self):
    #     input = """
    #     inc: function void(out n: integer, delta: integer) {
    #         if (n > delta) {
    #             if (true) {}
    #             else {}
    #         } else {
    #             if (n % 2.0 == 0) {}
    #         }
    #     }
    #     main: function void() {}
    #     """
    #     expect = "Type Mismatch In Expression: BinExpr(%, Id(n), FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input, expect, 428))

    # Test Assignment In function
    # def test_29(self):
    #     input = """
    #     x: integer;
    #     inc: function void(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         x = 1;
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 429))

    # def test_30(self):
    #     input = """
    #     x: integer;
    #     main: function void() {
    #         x = false;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(False))"
    #     self.assertTrue(TestChecker.test(input, expect, 430))

    # def test_31(self):
    #     input = """
    #     x: float;
    #     main: function void() {
    #         x = 1;
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 431))

    # def test_32(self):
    #     input = """
    #     main: function void() {
    #         x: float = 1;
    #         a: array[10] of integer = {1, 2, 3};
    #         x = a[1];
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 432))

    # def test_33(self):
    #     input = """
    #     x: integer;
    #     inc: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: float = inc(inc(), x);
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test_33(self):
    #     input = """
    #     x: integer;
    #     inc: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = inc(inc(x, x), x);
    #         y: integer = inc(x, 1) + 1;
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test_34(self):
    #     input = """
    #     x: integer;
    #     inc: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     inc1: function auto() {}
    #     main: function void() {
    #         delta: integer = inc(inc(x, x), x);
    #         y: integer = inc(x, delta) + inc1();
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    # def test_35(self):
    #     input = """
    #     x: integer;
    #     inc: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = inc(inc(x, x), x);
    #         y: bool = -inc(x, 1);
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 435))

    # def test_36(self):
    #     input = """
    #     x: integer;
    #     inc: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = 1;
    #         n1: float = -inc(x, delta) + 1; // inc: float
    #         n1: float = !inc(x, delta) + 1;
    #         n1: float = -inc(x, delta) < 8;
    #         n1: bool = -inc(x, 1);
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    # def test_37(self):
    #     input = """
    #     x: integer;
    #     a: array [10] of integer;
    #     inc: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = 1;
    #         delta = inc(delta, x);
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # def test_38(self):
    #     input = """
    #     x: integer;
    #     a: array [10] of integer;
    #     inc: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = 1;
    #         a[1] = inc(delta, x);
    #         x = (inc(delta, x) + a[1]) - 4;
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 438))

    # def test_39(self):
    #     input = """
    #     x: array[0, 100] of integer;
    #     inc: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = 1;
    #         i: integer = 1;
    #         if (x[i, 0] > inc(x[0, i])) {
    #             x[i, 0] = i;
    #         } else {
    #             x[0, i] = i + 1;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: FuncCall(Id(inc), [ArrayCell(Id(x), [IntegerLit(0), Id(i)])])"
    #     self.assertTrue(TestChecker.test(input, expect, 439))

    # def test_40(self):
    #     input = """
    #     foo: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         x: integer = 2;
    #         for (i = 1, i < 100, i+1) {
    #             foo(x + 1, foo(i + 1, foo(x + 2, 1)));
    #         }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 440))

    # def test_41(self):
    #     input = """
    #     foo: function auto(out n: integer, delta: integer) {
    #         n = n + delta;
    #         return 1;
    #     }
    #     main: function void() {
    #         return 1;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: ReturnStmt(IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 441))

    # def test_42(self):
    #     input = """
    #     foo2: function auto(i: integer){}
    #     foo1: function integer(){
    #         return 1;
    #     }

    #     main: function void(){
    #         foo2(foo1());
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 442))

    # def test_43(self):
    #     input = """
    #     foo2: function auto(inherit i: float, a: float){}
    #     foo1: function integer() {
    #         super(1, 1.0);
    #         return 1;
    #     }

    #     main: function void(){
    #         foo2(foo1());
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: CallStmt(Id(super), [IntegerLit(1), FloatLit(1.0)])"
    #     self.assertTrue(TestChecker.test(input, expect, 443))

    # def test_44(self):
    #     input = """
    #     foo2: function auto(inherit i: float, a: float){}
    #     foo1: function integer() inherit foo2 {
    #         super(1, true);
    #         return 1;
    #     }

    #     main: function void(){
    #         foo2(foo1());
    #     }
    #     """
    #     expect = "Invalid Statement In Function: foo1"
    #     self.assertTrue(TestChecker.test(input, expect, 444))

    # def test_44(self):
    #     input = """
    #     foo2: function auto(inherit i: float, a: float){}
    #     foo1: function integer() inherit foo2 {
    #         return 1;
    #     }

    #     main: function void(){
    #         foo2(foo1());
    #     }
    #     """
    #     expect = "Invalid Statement In Function: foo1"
    #     self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """
        foo3: function auto(inherit i: integer, a: float) {}
        foo2: function auto(inherit i: float, a: float) inherit foo3 {
            super(1, 1.0);
        }
        foo1: function integer() inherit foo2 {
            // preventDefault();
            super(1, 1.0);
            //preventDefault(1, 2, 3);
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2(foo1());
        }
        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, 445))
