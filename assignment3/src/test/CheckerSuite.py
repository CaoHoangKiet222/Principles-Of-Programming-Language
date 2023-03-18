import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # Test VarDecl
    def test_1(self):
        input = """
        a: float;
        x: integer = a + 2;
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), IntegerType, BinExpr(+, Id(a), IntegerLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """
        c: integer = 2.3;
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), IntegerType, FloatLit(2.3))"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """
        c: float = 2.3;
        c: string;
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """
        a: auto = 10;
        c: auto = !(a < 100);
        c: auto = c;
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        input = """
        b: auto = "hello";
        c: auto = b == "hello1";
        """
        expect = "Type Mismatch In Expression: BinExpr(==, Id(b), StringLit(hello1))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        input = """
        b: auto = true;
        c: auto;
        """
        expect = "Invalid Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 406))

    # Not update assignment yet
    def test_7(self):
        input = """
        b: auto = 1 == true;
        c: auto = b == false;
        """
        expect = "Type Mismatch In Expression: BinExpr(==, IntegerLit(1), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """
        x: integer = 9_9999_999;
        y: integer = x == 1;
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(y), IntegerType, BinExpr(==, Id(x), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        input = """
        a: array [2] of integer = {1, 2};
        b: array [2, 3] of integer = {{}, {}};
        c: array [2, 3] of integer = {{1}, {1, 2, 3}};
        d: array [2, 3, 5] of integer = {{{1, 3, 4}, {5, 6}, {}}, {{1}, {2}, {1}}};
        e: array [2, 3] of integer = {{1.0}, {1, 2, 3}};
        f: array [2, 3] of integer = {{1, 1}, {1.0, 2, 3}};
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(e), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self):
        input = """
        x, y, z: integer = 1, 2, 3;
        a: array [3, 2] of integer = {{x + z}, {y, z}};
        b: array [2, 3] of integer = {1, {1, 3, 4}};
        """
        expect = "Illegal Array Literal: ArrayLit([IntegerLit(1), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4)])])"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """
        a: array [2, 3] of float = {{1}, {1, 3, 4}};
        b: array [2, 3] of integer = {{1.0}, {1.0, 3.0, 4.0}};
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([FloatLit(1.0), FloatLit(3.0), FloatLit(4.0)])]))"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """
        a: array [2, 3] of integer = {{1}, {1, 3, 4}};
        b: array [2, 3] of integer = {{}};
        c: array [2, 3] of integer = {{}, {}, {}};
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([])]))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """
        a: array [2, 3] of integer = {{1}, {1, 3, 4, 5}};
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4), IntegerLit(5)])]))"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        input = """
        a: array [2, 3, 2] of integer = {{{}, {}, {}, {}}, {{}, {}, {}}};
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2, 3, 2], IntegerType), ArrayLit([ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([])]), ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([])])]))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """
        a: array [2, 3] of boolean = {};
        b: array [2, 3] of boolean = {{}};
        c: array [2, 3] of boolean = {{true}, {false}};
        d: array [2, 3] of boolean = {{false, false}, {1}};
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(d), ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([BooleanLit(False), BooleanLit(False)]), ArrayLit([IntegerLit(1)])]))"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        input = """
        e: array [2, 3] of boolean = {false, true, true}; // -> dont know ask teacher
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(e), ArrayType([2, 3], BooleanType), ArrayLit([BooleanLit(False), BooleanLit(True), BooleanLit(True)]))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
        a: array[3] of integer = {1};
        b: integer = a[0] + 2;
        b: integer = -a[0, 1] + 2;
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 417))

    # Test Function Declare
    def test_18(self):
        input = """
        main: function void() {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """
        inc: function void(out n: integer, delta: integer) {}
        main: function void() {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
        inc: function void(delta: integer, delta: float) {}
        main: function void() {}
        """
        expect = "Redeclared Parameter: delta"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """
        inc: function void() {}
        inc: function void(out n: integer, delta: float) {}
        main: function void() {}
        """
        expect = "Redeclared Function: inc"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """
        inc: function void(out n: integer, delta: float) {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """
        inc: function void(out n: integer, delta: integer) {
            x, y, z: integer;
            a: auto = x;
        }
        main: function void() {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """
        inc: function void(out n: integer, delta: integer) {
            a: auto;
        }
        main: function void() {}
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """
        inc: function void(out n: integer, delta: integer) {
            x, y, z: integer;
            a, b, c: boolean;
            n: integer;
        }
        main: function void() {}
        """
        expect = "Redeclared Variable: n"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """
        inc: function void(out n: integer, delta: integer) {
            x, y, z: integer;
            a, b, c: boolean;
            n: integer;
        }
        main: function void() {}
        """
        expect = "Redeclared Variable: n"
        self.assertTrue(TestChecker.test(input, expect, 426))

    # Test IfStmt in Function
    def test_27(self):
        input = """
        inc: function void(out n: integer, delta: integer) {
            if (n > delta) {
            } else {}
        }
        main: function void() {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """
        inc: function void(out n: integer, delta: integer) {
            if (n > delta) {
                if (true) {}
                else {}
            } else {
                if (n % 2.0 == 0) {}
            }
        }
        main: function void() {}
        """
        expect = "Type Mismatch In Expression: BinExpr(%, Id(n), FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    # Test Assignment In function
    def test_29(self):
        input = """
        x: integer;
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            x = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """
        x: integer;
        main: function void() {
            x = false;
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        input = """
        x: float;
        main: function void() {
            x = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """
        main: function void() {
            x: float = 1;
            a: array[10] of integer = {1, 2, 3};
            x = a[1];
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """
        x: integer;
        inc: function auto(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = inc(inc(x, x), x);
            y: integer = inc(x, 1) + 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        input = """
        x: integer;
        inc: function auto(out n: integer, delta: integer) {
            n = n + delta;
        }
        inc1: function auto() {}
        main: function void() {
            delta: integer = inc(inc(x, x), x);
            y: integer = inc(x, delta) + inc1();
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        input = """
        x: integer;
        inc: function auto(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = inc(inc(x, x), x);
            y: boolean = -inc(x, 1);
        }
        """
        expect = "not check"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input = """
        x: integer;
        inc: function auto(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = 1;
            n1: float = -inc(x, delta) + 1; // inc: float
            n1: float = !inc(x, delta) + 1;
            n1: float = -inc(x, delta) < 8;
            n1: boolean = -inc(x, 1);
        }
        """
        expect = "not check"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """
        x: integer;
        a: array [10] of integer;
        inc: function auto(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = 1;
            delta = inc(delta, x);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """
        x: integer;
        a: array [10] of integer;
        inc: function auto(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = 1;
            a[1] = inc(delta, x);
            x = (inc(delta, x) + a[1]) - 4;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """
        x: array[0, 100] of integer;
        inc: function auto(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = 1;
            i: integer = 1;
            if (x[i, 0] > inc(x[0, i])) {
                x[i, 0] = i;
            } else {
                x[0, i] = i + 1;
            }
        }
        """
        expect = "Type Mismatch In Expression: FuncCall(Id(inc), [ArrayCell(Id(x), [IntegerLit(0), Id(i)])])"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """
        foo: function auto(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            x: integer = 2;
            for (i = 1, i < 100, i+1) {
                foo(x + 1, foo(i + 1, foo(x + 2, 1)));
            }
        }
        """
        expect = "Type Mismatch In Expression: FuncCall(Id(foo), [BinExpr(+, Id(i), IntegerLit(1)), FuncCall(Id(foo), [BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(1)])])"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """
        foo: function auto(out n: integer, delta: integer) {
            n = n + delta;
            return 1;
        }
        main: function void() {
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """
        foo2: function auto(i: integer){}
        foo1: function integer(){
            return 1;
        }

        main: function void(){
            foo2(foo1());
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
        foo2: function auto(inherit i: float, a: float){}
        foo1: function integer() {
            super(1, 1.0);
            return 1;
        }

        main: function void(){
            foo2(foo1());
        }
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(super), [IntegerLit(1), FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """
        foo2: function auto(inherit i: float, a: float){}
        foo1: function integer() inherit foo2 {
            super(1, true);
            return 1;
        }

        main: function void(){
            foo2(foo1());
        }
        """
        expect = "Invalid Statement In Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """
        foo2: function auto() {}
        foo1: function integer(inherit c: float) inherit foo2 {
            super();
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2();
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        input = """
        foo2: function auto() {}
        foo1: function integer(inherit c: float) inherit foo2 {
            preventDefault(1, 2, 3);
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2();
        }
        """
        expect = "Invalid Statement In Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """
        foo2: function auto(inherit a: integer) {}
        foo1: function integer(inherit c: float) inherit foo2 {
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2(1);
        }
        """
        expect = "Invalid Statement In Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        input = """
        foo3: function auto(inherit i: integer, a: float) {}
        foo2: function auto(inherit b: float, a: float) inherit foo3 {
            super(true, 1.0);
        }
        foo1: function integer(inherit c: float) inherit foo2 {
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2(foo1(1.0), 1);
        }
        """
        expect = "Invalid Statement In Function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        input = """
        foo3: function auto(inherit i: integer, a: float) {}
        foo2: function auto(inherit b: float, a: float) inherit foo3 {
            super(1, 1.0);
            c: integer = 1;
        }
        foo1: function integer(inherit c: float) inherit foo2 {
            super(1, 1.0);
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2(foo1(1.0), 1);
        }
        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """
        foo3: function auto(inherit i: integer, a: float) {}
        foo2: function auto(inherit b: float, a: float) inherit foo3 {
            super(1, 1.0);
            c: integer = 1;
        }
        foo1: function integer(inherit c: float) inherit foo2 {
            preventDefault();
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2(foo1(1.0), 1);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        input = """
        foo2: function auto() {}
        foo1: function integer(inherit c: float) inherit foo2 {
            printInteger(super(1.0, 1.0));
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2(foo1(1.0), 1);
        }
        """
        expect = "Type Mismatch In Expression: FuncCall(Id(super), [FloatLit(1.0), FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_52(self):
        input = """
        foo2: function auto() {}
        foo1: function integer(inherit c: float) inherit foo2 {
            printInteger(foo2());
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2();
        }
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo2), [])"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """
        x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 453))

    # Test Parameter
    def test_54(self):
        input = """
        inherit out  x: integer
        main: function void() {
        }
        """
        expect = "Invalid Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 454))

    # Test Mix
    def test_55(self):
        input = """
        main: function void() {
            break;
        }
        """
        expect = "BreakStmt() Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_56(self):
        input = """
        main: function void() {
            continue;
        }
        """
        expect = "ContinueStmt() Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input = """
        main: function void() {
            for (i = 1, i < 100, i+1) {
                j : integer = 0;
                while (200) {j = j+1;}
                while (i != 20) {}
            }
        }
        """
        expect = "Type Mismatch In Statement: WhileStmt(IntegerLit(200), BlockStmt([AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_59(self):
        input = """
        main: function void(out x: array[0, 100] of integer) {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_60(self):
        input = """
        main: function void() {
            x: array[4, 10, 10] of integer;
            for (i = 1, i < 100, i+1) {
                if (i % 2 == 0) {
                    x[i, 0, 1] = i;
                } else {
                    x[0, i] = i + 1;
                }
                for(j = 1, j < 100, j+1) {
                }
                while(true) {continue;}
                break;
            }
            continue;
        }
        """
        expect = "ContinueStmt() Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = """
        Check: function boolean (nums: array[100] of integer, size: integer) {
          count: integer  = 0;
          for (i = 0, i < size, i + 1) {
            if (nums[i] < 0)
              count = count + 1;
          }
          if (count % 2 == 0)
            return true;
          else
            return "hello";
        }

        main: function void() {
            nums: array[100] of integer;
            printBoolean(Check(nums, 100));
        }
        """
        expect = "Type Mismatch In Statement: ReturnStmt(StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        input = """
        reverseStr: function string(str: string, size: integer) {
            for (i = 0, i < size / 2, i+1) {
                x : string = str[i];
                str[i] = str[size - i - 1];
                str[size - i - 1] = x;
            }
            return str;
        }

        main: function void() {
            printString(reverseStr("123", 3));
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(str), [Id(i)])"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        input = """
        test: function string(str: string, size: integer) {
            i: boolean = true;
            for (i = 0, i < size / 2, i+1) {
                i: integer = 1;
                i = false;
            }
            return str;
        }

        main: function void() {
            printString(test("123", 3));
        }
        """
        expect = "Type Mismatch In Statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(size), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(i), IntegerType, IntegerLit(1)), AssignStmt(Id(i), BooleanLit(False))]))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_64(self):
        input = """
        test: function string(str: string, size: integer) {
            j: boolean = true;
            for (i = 0, i < size / 2, i+1) {
                j: integer = 1;
                j = false;
            }
            return str;
        }

        main: function void() {
            printString(test("123", 3));
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(j), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_65(self):
        input = """
        checkDuplicate: function boolean(ar: array[100] of integer, size: integer) {
          if (size <= 1)
            return true;
          less, greater: array[1000] of integer;
          greater_size, less_size: integer  = 0, 0;

          for (i = 1, i < size, i+1) {
            if (ar[i] == ar[0]) {
              return false;
            }

            if (ar[i] < ar[0]) {
              less[less_size] = ar[i];
              less_size = less_size + 1;
            } else {
              greater[greater_size] = ar[i];
              greater_size = greater_size + 1;
            }
          }

          return checkDuplicate(less, less_size) +
                 checkDuplicate(greater, greater_size);
        }

        main: function void() {
        }
        """
        expect = "Type Mismatch In Expression: BinExpr(+, FuncCall(Id(checkDuplicate), [Id(less), Id(less_size)]), FuncCall(Id(checkDuplicate), [Id(greater), Id(greater_size)]))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_66(self):
        input = """
        less_zero: boolean = false;
        c: integer = 0;

        printegerPattern: function void(n: integer) {
          if (n <= 0) {
            less_zero = true;
          }

          if (less_zero) {
            c = c - 1;
            if (c == -1)
              return;
            printegerPattern(n + 5);
          } else {
            c = c + 1;
            printegerPattern(n - 5);
          }
        }
        main: function void() {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        input = """
        checkElementsUniqueness: function auto (arr: array[100] of integer, n: integer) {
          if ((n > 1000) || (n < 0))
            return false;
          for (i = 0, i < n - 1, i+1) {
            for (j = i + 1, j < n, j+1) {
              if (arr[i] == arr[j])
                return false;
            }
          }
          return true;
        }

        main: function void() {
            arr   : array [6] of integer = {1, 91, 0, -100, 100, 200};
            if (checkElementsUniqueness(arr, 6)) printString("Correct!");
            else printString("Wrong!");
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        input = """
        moduloDivision: function integer(seed: integer, mod: float) { return seed % mod; }

        main: function void() {
        }
        """
        expect = "Type Mismatch In Expression: BinExpr(%, Id(seed), Id(mod))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = """
        swap: function void(x: float,y: float) {
          k: integer = x;
          x = y;
          y = k;
        }

        main: function void() {
            swap(1, 2);
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(k), IntegerType, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = """
        numIsPrime: function boolean (n : integer) {
          if (n < 2)
            return false;
          for (i = 2, i <= sqrt(n), i+1) {
            if (n % i == 0)
              return false;
          }
          return true;
        }

        main: function void() {
        }
        """
        expect = "Undeclared Function: sqrt"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_71(self):
        input = """
        inc : function void (out n: integer, delta : integer) {
            nE : integer = 0;
            do {
                for (i = 0, i < nE, i + 1)
                    if (nE == 10 + 5)
                        return nE;
                    else
                        nE = nE + 1;
                    continue;
            } while(true);
        }

        main: function void() {
        }
        """
        expect = "Type Mismatch In Statement: ReturnStmt(Id(nE))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = """
        inc : function auto (out n: integer, delta : integer) {
            nE : integer = 0;
            do {
                for (i = 0, i < nE, i + 1)
                    if (nE == 10 + 5)
                        return nE;
                    else
                        nE = nE + 1;
            } while(true);
            continue;
        }

        main: function void() {
        }
        """
        expect = "ContinueStmt() Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_73(self):
        input = """
        sum: function integer(n: integer)
        {
            total,dem : integer = 0,0;
            do
            {
                total = total + (n%10);
                dem = dem + 1;
                n = n % 10;
            }
            while (n!=0);
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            n = readInteger();
            printString("The sum is" + sum(n));
        }
        """
        expect = "Type Mismatch In Expression: BinExpr(+, StringLit(The sum is), FuncCall(Id(sum), [Id(n)]))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        input = """
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + randomChar();
            return s;
        }
        main: function void() {
            n : integer;
            print("Input n:");
            readInt(n);
            print("The random string length n is ", random(n));
        }
        """
        expect = "Undeclared Function: randomChar"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_75(self):
        input = """
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + random(i);
            return s;
        }
        main: function void() {
        }
        """
        expect = "Type Mismatch In Expression: BinExpr(+, Id(s), FuncCall(Id(random), [Id(i)]))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_76(self):
        input = """
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s::random(i);
            return s;
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            n = readInteger();
            printString("The random string length n is "::random(n));
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        input = """
        foo: function float (n : integer, inherit out a: float) {
            return true;
        }
        main: function void (out m : float, out a: float) inherit foo {
            continue;
            return true;
        }
        """
        expect = "Type Mismatch In Statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):
        input = """
        foo: function boolean (n : integer, inherit out a: float) {
            return true;
        }
        main: function void (out m : float, out a: float) inherit foo {
            continue;
            return true;
        }
        """
        expect = "Invalid Statement In Function: main"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        input = """
        foo: function boolean () {
            return true;
        }
        main: function void (out m : float, out a: float) inherit foo {
            return true;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_80(self):
        input = """
        main : function void () {
            nE : integer = 0;
            for (i = 0, i < nE, i + 1)
                if (nE == (10 + 5))
                    return nE;
                else i = i + 1;
        }
        """
        expect = "Type Mismatch In Statement: ReturnStmt(Id(nE))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = """
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            return f[1];
        }
        bar: function void (inherit out a: integer, inherit out b: string) inherit foo {
            super("Hello", 123);
            for (i = 1, i < 10, i + 1)
            {
                printFloat(a);
            }
            if (a==2)
                return;
            else
                break;
        }
        main : function void () {
        }
        """
        expect = "Undeclared Function: printFloat"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_82(self):
        input = """
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            return f[1];
        }
        bar: function void (inherit out a: integer, inherit out b: string) inherit foo {
            super("Hello", 123);
            for (i = 1, i < 10, i + 1)
            {
                writeFloat(a);
            }
            if (a==2)
                return;
            else
                break;
        }
        main : function void () {
        }
        """
        expect = "BreakStmt() Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = """
        inc: function auto(inherit a: integer, b: integer)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            return a;
            do
            {
                a = b + 1;
            }
            while (a==true);
        }
        main: function void() inherit inc {
        }
        """
        expect = "Type Mismatch In Expression: BinExpr(==, Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 483))

        def test_84(self):
            input = """
        x: float = 3.0;
        a : array [2] of integer;
        foo: function auto(){}
        fact : function integer (n : integer) {
            b: float;
            n = foo() + 1;
        }
        main: function void() inherit fact {
        }
    """

            expect = "Invalid Statement In Function: main"
            self.assertTrue(TestChecker.test(input, expect, 484))

        def test_85(self):
            input = """
        fact : function integer (n : integer) {
            a : array [2] of integer;
            i: float = 3;
            for (i = 123, 9 > 8, i + 1){}
        }
        main: function void(){}
    """
            expect = "Type Mismatch In Statement: ForStmt(AssignStmt(Id(i), IntegerLit(123)), BinExpr(>, IntegerLit(9), IntegerLit(8)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"
            self.assertTrue(TestChecker.test(input, expect, 485))

    def test_86(self):
        input = """
        foo2: function boolean(i: integer){}
        main: function void() inherit foo2 {
            super(1);
            for (i = 123, i > 8, foo2(1)){}
        }
    """

        expect = "Type Mismatch In Statement: ForStmt(AssignStmt(Id(i), IntegerLit(123)), BinExpr(>, Id(i), IntegerLit(8)), FuncCall(Id(foo2), [IntegerLit(1)]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = """
        foo2: function integer(inherit i: boolean){}
        main: function void() inherit foo2 {
            super(true);
            for (i = 123, i > 8, foo2(true)){}
        }
    """

        expect = "Type Mismatch In Statement: ForStmt(AssignStmt(Id(i), IntegerLit(123)), BinExpr(>, Id(i), IntegerLit(8)), FuncCall(Id(foo2), [BooleanLit(True)]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        input = """
        x: integer;
        foo1: function integer(inherit x: float){}
        foo2: function float(inherit y: float){
            super(10);
            z: float = 10.1;
            return 1;
        }
        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Type Mismatch In Statement: CallStmt(Id(super), [IntegerLit(10)])"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """
        x: integer;
        haha: function integer(){}

        haha1: function float(inherit y: float) inherit haha{
            z: float = 10_999_222_1.1;
            return 1;
        }
        main: function void() inherit haha {
            preventDefault();
            x: integer = readInteger();
            printInteger(x);
        }
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """
        x: integer;
        foo1: function integer(inherit y: integer){}

        foo2: function float(inherit z: float) inherit foo1{
            super(10);
            y: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """
        x: integer;
        jump: function integer(inherit nums: array[100] of integer, size: integer){
          minjump: integer = size - 1;
          return minjump;
        }

        jump_: function float(inherit z: float) inherit jump {
            preventDefault();
            y: float = 10.1;
            return nums[0];
        }

        main: function void(){
        }
    """

        expect = "Undeclared Identifier: nums"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        input = """
        a,b: array[10] of integer;
        swap: function void(out a: array[10] of integer, out b: array[10] of integer, n: integer)
        {
            if (n>10)
                return;
            else
            {
                temp,i : integer;
                for (i=0,i<n,i+1)
                {
                    temp=a[i];
                    a[i]=b[i];
                    b[i]=temp;
                }
            }
        }
        main: function void() {
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 492))

        def test_93(self):
            input = """

        foo1: function integer(){}

        foo2: function float(inherit x: boolean) inherit foo1{
            return 1;
        }
        foo3: function float() inherit foo2{
            super(false);
            preventDefault();
            x: float = 10.2;
            return 1.123;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """
            expect = "Redeclared Variable: x"
            self.assertTrue(TestChecker.test(input, expect, 493))

        def test_94(self):
            input = """
        isPalindrome: function boolean(strs: array[100] of string, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
              return false;
            }
          }
          return true;
        }
        main: function void() {
            strs   : array [5] of string = {"hello", "world", "!!!", "", "test\\n"};

            if(isPalindrome(strs, 5)) printString("Correct!!!");
            else printString("Wrong!!!");
        }
    """
            expect = "Type Mismatch In Expression: BinExpr(!=, ArrayCell(Id(strs), [Id(i)]), ArrayCell(Id(strs), [BinExpr(-, BinExpr(-, Id(strSize), Id(i)), IntegerLit(1))]))"
            self.assertTrue(TestChecker.test(input, expect, 494))

        def test_95(self):
            input = """
        isPalindrome: function boolean(strs: array[100] of string, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
              return false;
            }
          }
          return true;
        }
        main: function void() {
            strs   : array [5] of string = {"hello", "world", "!!!", "", "test\\n"};
            if(isPalindrome(strs, 5)) printString("Correct!!!");
            else printString("Wrong!!!");
        }
    """
            expect = "Type Mismatch In Expression: BinExpr(!=, ArrayCell(Id(strs), [Id(i)]), ArrayCell(Id(strs), [BinExpr(-, BinExpr(-, Id(strSize), Id(i)), IntegerLit(1))]))"
            self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = """
        foo2: function auto(inherit i: float, a: float){}
        foo1: function integer() inherit foo2 {
            return 1;
        }

        main: function void(){
            foo2(foo1());
        }
        """
        expect = "Invalid Statement In Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_97(self):
        input = """
        containStr: function boolean (S1: string , S2: string, sizeS1: integer, sizeS2: integer) {
          b : array[1000] of boolean;
          for (i = 0, i < sizeS2, i + 1) {
            found: boolean = false;
            for (j = 0, j < sizeS1, j + 1) {
              if (!b[j]) {
                if (S2[i] == S1[j]) {
                  found = false;
                  b[j] = false;
                }
              }
            }
            if (!found) {
              return false;
            }
          }
          return false;
        }

        main: function void(){
        }
    """
        expect = "Type Mismatch In Expression: ArrayCell(Id(S2), [Id(i)])"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_98(self):
        input = """
        search: function integer(nums: array[100] of integer, size: integer, target: integer) {
            left, right: integer = 0, size - 1;
            index: integer = -1;
            found: boolean = false;
            while (left <= right && !found) {
              mid: integer = (left + right) / 2;
              if (nums[mid] == target) {
                found = false;
                index = mid;
              }
              if (nums[mid] >= nums[left]) {
                if (nums[mid] > target) {
                  if (target < nums[left])
                    left = mid + 1;
                  else
                    right = mid - 1;
                } else
                  left = mid + 1;
              } else {
                if (target > nums[mid]) {
                  if (target > nums[right])
                    right = mid - 1;
                  else
                    left = mid + 1;
                } else
                  right = mid - 1;
              }
            }
            return index;
        }

        main: function void(){
        }
    """
        expect = "Type Mismatch In Expression: BinExpr(&&, Id(right), UnExpr(!, Id(found)))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_99(self):
        input = """
        max_two_nums: function auto (a: integer, b: integer) {
            if (a > b) {
                return a;
            }
            return b;
        }

        main: function void(){
            max_two_nums(1, 1);
        }
    """
        expect = "Type Mismatch In Statement: CallStmt(Id(max_two_nums), [IntegerLit(1), IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_100(self):
        input = r"""
    foo: function string (a: string, b: float) {
        c : integer = 2;
        d: float = c + 1;
        f : array [5] of string;
        return f[1];
    }
    bar: function void (inherit out a: float, inherit out b: string) inherit foo {
        super("Hello", 123);
        for (i = 1, i < 10, i + 1)
        {
            writeFloat(a);
        }
        if (a==2)
            return;
        else
            break;
    }
    main: function void() {}
"""
        expect = "Type Mismatch In Expression: BinExpr(==, Id(a), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 500))
