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
	VarDecl(Id(a), ArrayType([2, 3], IntegerType))
	VarDecl(Id(b), ArrayType([2, 3], IntegerType))
	VarDecl(Id(c), ArrayType([2, 3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6(self):
        input = """
        a, b, c: array [2, 3] of integer = {{1, 2, 3}, {0, 5, 6}}, {{}, {}}, {{2, 3}, {}};
"""
        expect = """Program([
	VarDecl(Id(a), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(0), IntegerLit(5), IntegerLit(6)])]))
	VarDecl(Id(b), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7(self):
        input = """
        a2, b2, c2   : array [2, 3] of float = {{1.33333, .5555e-1, 189.00000}, {157., 1_2_3_4., 1_2_3_56.1234}}, {{}, {}}, {{1.34, 12e8}, {}};
"""
        expect = """Program([
	VarDecl(Id(a2), ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.33333), FloatLit(.5555e-1), FloatLit(189.00000)]), ArrayLit([FloatLit(157.), FloatLit(1234.), FloatLit(12356.1234)])]))
	VarDecl(Id(b2), ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c2), ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.34), FloatLit(12e8)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input = """
        a, b, c : array [2, 3] of string = {{"x", "y"}, {"z"}}, {{}, {}}, {{"hello", "world"}, {"hihi"}};
"""
        expect = """Program([
	VarDecl(Id(a), ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(x), StringLit(y)]), ArrayLit([StringLit(z)])]))
	VarDecl(Id(b), ArrayType([2, 3], StringType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c), ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(hello), StringLit(world)]), ArrayLit([StringLit(hihi)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = """
        a, b, c : array [2] of boolean = {false, true}, {true}, {false};
"""
        expect = """Program([
	VarDecl(Id(a), ArrayType([2], BooleanType), ArrayLit([BooleanLit(False), BooleanLit(False)]))
	VarDecl(Id(b), ArrayType([2], BooleanType), ArrayLit([BooleanLit(False)]))
	VarDecl(Id(c), ArrayType([2], BooleanType), ArrayLit([BooleanLit(False)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """
        a, b, c : integer = -1, 0, 3;
        y, z : integer = 1, 1;
        x : array [0, 100] of integer;
"""
        expect = """Program([
	VarDecl(Id(a), IntegerType, UnExpr(-, IntegerLit(1)))
	VarDecl(Id(b), IntegerType, IntegerLit(0))
	VarDecl(Id(c), IntegerType, IntegerLit(3))
	VarDecl(Id(y), IntegerType, IntegerLit(1))
	VarDecl(Id(z), IntegerType, IntegerLit(1))
	VarDecl(Id(x), ArrayType([0, 100], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    # # # Test Function Declarations # # #
    def test_11(self):
        input = """main: function void () {}"""
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(printInteger), IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13(self):
        input = """
        main: function void() {
            found : boolean = true;
            is_Num, is_String: string = "", "";
            is_String = "TEST";
        }
    """
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(found), BooleanType, BooleanLit(False)), VarDecl(Id(is_Num), StringType, StringLit()), VarDecl(Id(is_String), StringType, StringLit()), AssignStmt(Id(is_String), StringLit(TEST))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = """
        main: function void() {
            x : integer = 1;
            for (i = 1, i < 100, i+1) {
                foo(x + 1, foo(i + 1, foo(x + 2, 1)));
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(x), IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(Id(foo), BinExpr(+, Id(x), IntegerLit(1)), FuncCall(Id(foo), [BinExpr(+, Id(i), IntegerLit(1)), FuncCall(Id(foo), [BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(1)])]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = """
        main: function void() {
            for (i = 1, i < 100, i+1) {
                j : integer = 0;
                while (j < 200) {j = j+1;}
                while (i != 20) {}
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(j), IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(j), IntegerLit(200)), BlockStmt([AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), WhileStmt(BinExpr(!=, Id(i), IntegerLit(20)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """
        main: function void(out x: array[0, 100] of integer) {}
    """
        expect = """Program([
	FuncDecl(Id(main), VoidType, [OutParam(Id(x), ArrayType([0, 100], IntegerType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17(self):
        input = """
        lengthOfFirstWord: function auto() {return "";}
        lengthOfLastWord: function auto() inherit lengthOfFirstWord {
            return "lengthOfLastWord";
        }
    """
        expect = """Program([
	FuncDecl(Id(lengthOfFirstWord), AutoType, [], None, BlockStmt([ReturnStmt(StringLit())]))
	FuncDecl(Id(lengthOfLastWord), AutoType, [], Id(lengthOfFirstWord), BlockStmt([ReturnStmt(StringLit(lengthOfLastWord))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = """
        main: function void(out x: array[0, 100] of integer) {
            for (i = 1, i < 100, i+1) {
                if (i % 2 == 0) {
                    x[i, 0] = i;
                } else {
                    x[0, i] = i + 1;
                }
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(main), VoidType, [OutParam(Id(x), ArrayType([0, 100], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(Id(x), [Id(i), IntegerLit(0)]), Id(i))]), BlockStmt([AssignStmt(ArrayCell(Id(x), [IntegerLit(0), Id(i)]), BinExpr(+, Id(i), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = """
        main: function void(out x: integer) {
            for (i = 1, i < 100, i+1) {
                for (j = 1, j < 200, j+1) {
                    if (i + j >= 2) {
                        foo(2, x + 1);
                    }
                }
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(main), VoidType, [OutParam(Id(x), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(200)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, Id(i), Id(j)), IntegerLit(2)), BlockStmt([CallStmt(Id(foo), IntegerLit(2), BinExpr(+, Id(x), IntegerLit(1)))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """
        main: function void() {
            for (i = 1, i < 100, i+1) {
                for (j = 1, j < 200, j+1) {
                    if (i + j >= 2) {
                        break;
                    } else {
                        continue;
                    }
                }
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(200)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, Id(i), Id(j)), IntegerLit(2)), BlockStmt([BreakStmt()]), BlockStmt([ContinueStmt()]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """
        main: function void() {
            for (i = 1, i < 100, i+1) {
                j : integer = 0;
                while (j < 200) {
                    if (i + j >= 20) {
                        break;
                    } else {
                     j = j + 1;
                    }
                }
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(j), IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(j), IntegerLit(200)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, Id(i), Id(j)), IntegerLit(20)), BlockStmt([BreakStmt()]), BlockStmt([AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
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
            return false;
        }
    """
        expect = """Program([
	FuncDecl(Id(Check), BooleanType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(count), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(size)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(Id(nums), [Id(i)]), IntegerLit(0)), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1))))])), IfStmt(BinExpr(==, BinExpr(%, Id(count), IntegerLit(2)), IntegerLit(0)), ReturnStmt(BooleanLit(False)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
        input = """
        checkzero: function boolean(nums: array[100] of integer, size: integer) {
          found: boolean = false;
          for (i = 0, i < size && !found, i + 1) {
            if (nums[i] == 0)
              found = true;
          }
          if (found)
            return true;
          else
            return false;
        }
    """
        expect = """Program([
	FuncDecl(Id(checkzero), BooleanType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(found), BooleanType, BooleanLit(False)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(&&, Id(size), UnExpr(!, Id(found)))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(nums), [Id(i)]), IntegerLit(0)), AssignStmt(Id(found), BooleanLit(False)))])), IfStmt(Id(found), ReturnStmt(BooleanLit(False)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
        input = """
        Recursive: function void (nums: array[100] of integer, size: integer, index: integer , count: integer, sum: integer , minjump: integer) {
          if (sum >= size) {
            if (minjump > count)
              minjump = count;
          } else {
            for (i = 1, i <= nums[index], i + 1) {
              Recursive(nums, index + i, count + 1, sum + i, minjump);
            }
          }
        }
    """
        expect = """Program([
	FuncDecl(Id(Recursive), VoidType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType), Param(Id(index), IntegerType), Param(Id(count), IntegerType), Param(Id(sum), IntegerType), Param(Id(minjump), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(sum), Id(size)), BlockStmt([IfStmt(BinExpr(>, Id(minjump), Id(count)), AssignStmt(Id(minjump), Id(count)))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), ArrayCell(Id(nums), [Id(index)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(Id(Recursive), Id(nums), BinExpr(+, Id(index), Id(i)), BinExpr(+, Id(count), IntegerLit(1)), BinExpr(+, Id(sum), Id(i)), Id(minjump))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
        input = """
        jump: function integer(nums: array[100] of integer, size: integer) {
          minjump: integer = size - 1;
          Recursive(nums, 0, 0, 0, minjump);
          return minjump;
        }
    """
        expect = """Program([
	FuncDecl(Id(jump), IntegerType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(minjump), IntegerType, BinExpr(-, Id(size), IntegerLit(1))), CallStmt(Id(Recursive), Id(nums), IntegerLit(0), IntegerLit(0), IntegerLit(0), Id(minjump)), ReturnStmt(Id(minjump))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = """
        jump1: function integer(nums: array[100] of integer, size: integer) {
          curend, curfarthest, jumps: integer = 0, 0, 0;
          for (i = 0, i < size - 1, i + 1) {
            curfarthest = max(curfarthest, i + nums[i]);
            if (i == curend) {
              curend = curfarthest;
              jumps = jumps + 1;
            }
          }
          return jumps;
        }
    """
        expect = """Program([
	FuncDecl(Id(jump1), IntegerType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(curend), IntegerType, IntegerLit(0)), VarDecl(Id(curfarthest), IntegerType, IntegerLit(0)), VarDecl(Id(jumps), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(size), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(curfarthest), FuncCall(Id(max), [Id(curfarthest), BinExpr(+, Id(i), ArrayCell(Id(nums), [Id(i)]))])), IfStmt(BinExpr(==, Id(i), Id(curend)), BlockStmt([AssignStmt(Id(curend), Id(curfarthest)), AssignStmt(Id(jumps), BinExpr(+, Id(jumps), IntegerLit(1)))]))])), ReturnStmt(Id(jumps))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = """
        reverseStr: function string(str: string, size: integer) {
            for (i = 0, i < size / 2, i+1) {
                x : string = str[i];
                str[i] = str[size - i - 1];
                str[size - i - 1] = x;
            }
            return str;
        }
    """
        expect = """Program([
	FuncDecl(Id(reverseStr), StringType, [Param(Id(str), StringType), Param(Id(size), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(size), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(x), StringType, ArrayCell(Id(str), [Id(i)])), AssignStmt(ArrayCell(Id(str), [Id(i)]), ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(size), Id(i)), IntegerLit(1))])), AssignStmt(ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(size), Id(i)), IntegerLit(1))]), Id(x))])), ReturnStmt(Id(str))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = """
        lengthOfLastWord: function integer(s: array[100] of string, size: integer) {
            count: integer = 0;
            if (size == 0)
              return 0;
            i: integer = size - 1;
            while ((s[i] == " ") && i >= 0) {
              i = i - 1;
            }
            while ((i >= 0) && s[i] != " ") {
              count = count + 1;
              i = i - 1;
            }
            return count;
        }
    """
        expect = """Program([
	FuncDecl(Id(lengthOfLastWord), IntegerType, [Param(Id(s), ArrayType([100], StringType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(count), IntegerType, IntegerLit(0)), IfStmt(BinExpr(==, Id(size), IntegerLit(0)), ReturnStmt(IntegerLit(0))), VarDecl(Id(i), IntegerType, BinExpr(-, Id(size), IntegerLit(1))), WhileStmt(BinExpr(>=, BinExpr(&&, BinExpr(==, ArrayCell(Id(s), [Id(i)]), StringLit( )), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), WhileStmt(BinExpr(!=, BinExpr(&&, BinExpr(>=, Id(i), IntegerLit(0)), ArrayCell(Id(s), [Id(i)])), StringLit( )), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1))), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), ReturnStmt(Id(count))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = """
        containStr: function boolean (S1: string , S2: string, sizeS1: integer, sizeS2: integer) {
          b : array[1000] of boolean;
          for (i = 0, i < sizeS2, i + 1) {
            found: boolean = false;
            for (j = 0, j < sizeS1, j + 1) {
              if (!b[j]) {
                if (S2[i] == S1[j]) {
                  found = true;
                  b[j] = true;
                }
              }
            }
            if (!found) {
              return false;
            }
          }
          return true;
        }
    """
        expect = """Program([
	FuncDecl(Id(containStr), BooleanType, [Param(Id(S1), StringType), Param(Id(S2), StringType), Param(Id(sizeS1), IntegerType), Param(Id(sizeS2), IntegerType)], None, BlockStmt([VarDecl(Id(b), ArrayType([1000], BooleanType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(sizeS2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(found), BooleanType, BooleanLit(False)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(sizeS1)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, ArrayCell(Id(b), [Id(j)])), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(S2), [Id(i)]), ArrayCell(Id(S1), [Id(j)])), BlockStmt([AssignStmt(Id(found), BooleanLit(False)), AssignStmt(ArrayCell(Id(b), [Id(j)]), BooleanLit(False))]))]))])), IfStmt(UnExpr(!, Id(found)), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
        input = """
        search: function integer(nums: array[100] of integer, size: integer, target: integer) {
            left, right: integer = 0, size - 1;
            index: integer = -1;
            found: boolean = false;
            while (left <= right && !found) {
              mid: integer = (left + right) / 2;
              if (nums[mid] == target) {
                found = true;
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
    """
        expect = """Program([
	FuncDecl(Id(search), IntegerType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType), Param(Id(target), IntegerType)], None, BlockStmt([VarDecl(Id(left), IntegerType, IntegerLit(0)), VarDecl(Id(right), IntegerType, BinExpr(-, Id(size), IntegerLit(1))), VarDecl(Id(index), IntegerType, UnExpr(-, IntegerLit(1))), VarDecl(Id(found), BooleanType, BooleanLit(False)), WhileStmt(BinExpr(<=, Id(left), BinExpr(&&, Id(right), UnExpr(!, Id(found)))), BlockStmt([VarDecl(Id(mid), IntegerType, BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), IfStmt(BinExpr(==, ArrayCell(Id(nums), [Id(mid)]), Id(target)), BlockStmt([AssignStmt(Id(found), BooleanLit(False)), AssignStmt(Id(index), Id(mid))])), IfStmt(BinExpr(>=, ArrayCell(Id(nums), [Id(mid)]), ArrayCell(Id(nums), [Id(left)])), BlockStmt([IfStmt(BinExpr(>, ArrayCell(Id(nums), [Id(mid)]), Id(target)), BlockStmt([IfStmt(BinExpr(<, Id(target), ArrayCell(Id(nums), [Id(left)])), AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1))), AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1))))]), AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1))))]), BlockStmt([IfStmt(BinExpr(>, Id(target), ArrayCell(Id(nums), [Id(mid)])), BlockStmt([IfStmt(BinExpr(>, Id(target), ArrayCell(Id(nums), [Id(right)])), AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1))), AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1))))]), AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1))))]))])), ReturnStmt(Id(index))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
        input = """
        completeNum: function boolean(N: integer) {
          sum: integer = 0;
          for (i = 1, i < N, i + 1) {
            if (N % i == 0) {
              sum = sum + i;
            }
          }
          if (sum == N) {
            return true;
          }
          return false;
        }
    """
        expect = """Program([
	FuncDecl(Id(completeNum), BooleanType, [Param(Id(N), IntegerType)], None, BlockStmt([VarDecl(Id(sum), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(N)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(N), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))]))])), IfStmt(BinExpr(==, Id(sum), Id(N)), BlockStmt([ReturnStmt(BooleanLit(False))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
        input = """
        max_two_nums: function auto (a: integer, b: integer) { 
            if (a > b) {
                return a;
            }
            return b;
        }
    """
        expect = """Program([
	FuncDecl(Id(max_two_nums), AutoType, [Param(Id(a), IntegerType), Param(Id(b), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([ReturnStmt(Id(a))])), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33(self):
        input = """
        min_two_nums: function auto (a: integer, b: integer) { 
            if (a < b) {
                return a;
            }
            return b;
        }
    """
        expect = """Program([
	FuncDecl(Id(min_two_nums), AutoType, [Param(Id(a), IntegerType), Param(Id(b), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(a), Id(b)), BlockStmt([ReturnStmt(Id(a))])), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
        input = """
        factorial: function auto(N: integer) {
          result: integer = 1;
          for (i = 1, i <= N, i+1) {
            result = result * i;
          }
          return result;
        }
    """
        expect = """Program([
	FuncDecl(Id(factorial), AutoType, [Param(Id(N), IntegerType)], None, BlockStmt([VarDecl(Id(result), IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(N)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(*, Id(result), Id(i)))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35(self):
        input = """
        findMax: function auto(vals: array[100] of integer, numEls: integer) {
          max: integer = vals[0];
          for (i = 1, i < numEls, i+1) {
            if (vals[i] > max) {
              max = vals[i];
            }
          }
          return max;
        }
    """
        expect = """Program([
	FuncDecl(Id(findMax), AutoType, [Param(Id(vals), ArrayType([100], IntegerType)), Param(Id(numEls), IntegerType)], None, BlockStmt([VarDecl(Id(max), IntegerType, ArrayCell(Id(vals), [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(numEls)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(Id(vals), [Id(i)]), Id(max)), BlockStmt([AssignStmt(Id(max), ArrayCell(Id(vals), [Id(i)]))]))])), ReturnStmt(Id(max))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36(self):
        input = """
        findMin: function auto(vals: array[100] of integer, numEls: integer) {
          min: integer = vals[0];
          for (i = 1, i < numEls, i+1) {
            if (vals[i] < min) {
              min = vals[i];
            }
          }
          return min;
        }
    """
        expect = """Program([
	FuncDecl(Id(findMin), AutoType, [Param(Id(vals), ArrayType([100], IntegerType)), Param(Id(numEls), IntegerType)], None, BlockStmt([VarDecl(Id(min), IntegerType, ArrayCell(Id(vals), [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(numEls)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(Id(vals), [Id(i)]), Id(min)), BlockStmt([AssignStmt(Id(min), ArrayCell(Id(vals), [Id(i)]))]))])), ReturnStmt(Id(min))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_37(self):
        input = """
        isPalindrome: function boolean(str: array[100] of string, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (str[i] != str[strSize-i-1]) {
              return false;
            }
          }
          return true;
        }
    """
        expect = """Program([
	FuncDecl(Id(isPalindrome), BooleanType, [Param(Id(str), ArrayType([100], StringType)), Param(Id(strSize), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(strSize), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(Id(str), [Id(i)]), ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(strSize), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
        input = """
        checkElementsUniqueness: function boolean (arr: array[100] of integer, n: integer) {
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
    """
        expect = """Program([
	FuncDecl(Id(checkElementsUniqueness), BooleanType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(>, Id(n), IntegerLit(1000)), BinExpr(<, Id(n), IntegerLit(0))), ReturnStmt(BooleanLit(False))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(j)])), ReturnStmt(BooleanLit(False)))]))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39(self):
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

          return checkDuplicate(less, less_size) &&
                 checkDuplicate(greater, greater_size);
        }
    """
        expect = """Program([
	FuncDecl(Id(checkDuplicate), BooleanType, [Param(Id(ar), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(size), IntegerLit(1)), ReturnStmt(BooleanLit(False))), VarDecl(Id(less), ArrayType([1000], IntegerType)), VarDecl(Id(greater), ArrayType([1000], IntegerType)), VarDecl(Id(greater_size), IntegerType, IntegerLit(0)), VarDecl(Id(less_size), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(size)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(ar), [Id(i)]), ArrayCell(Id(ar), [IntegerLit(0)])), BlockStmt([ReturnStmt(BooleanLit(False))])), IfStmt(BinExpr(<, ArrayCell(Id(ar), [Id(i)]), ArrayCell(Id(ar), [IntegerLit(0)])), BlockStmt([AssignStmt(ArrayCell(Id(less), [Id(less_size)]), ArrayCell(Id(ar), [Id(i)])), AssignStmt(Id(less_size), BinExpr(+, Id(less_size), IntegerLit(1)))]), BlockStmt([AssignStmt(ArrayCell(Id(greater), [Id(greater_size)]), ArrayCell(Id(ar), [Id(i)])), AssignStmt(Id(greater_size), BinExpr(+, Id(greater_size), IntegerLit(1)))]))])), ReturnStmt(BinExpr(&&, FuncCall(Id(checkDuplicate), [Id(less), Id(less_size)]), FuncCall(Id(checkDuplicate), [Id(greater), Id(greater_size)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_40(self):
        input = """
        gcdIteration: function integer(p: integer, q: integer) {
          while (p * q != 0) {
            if (p > q) {
              p = p % q;
            } else {
              q = q % p;
            }
          }
          return p + q;
        }
    """
        expect = """Program([
	FuncDecl(Id(gcdIteration), IntegerType, [Param(Id(p), IntegerType), Param(Id(q), IntegerType)], None, BlockStmt([WhileStmt(BinExpr(!=, BinExpr(*, Id(p), Id(q)), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(>, Id(p), Id(q)), BlockStmt([AssignStmt(Id(p), BinExpr(%, Id(p), Id(q)))]), BlockStmt([AssignStmt(Id(q), BinExpr(%, Id(q), Id(p)))]))])), ReturnStmt(BinExpr(+, Id(p), Id(q)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41(self):
        input = """
        gcdRecursion: function integer(p: integer, q: integer) {
          if (q == 0)
            return p;
          return gcdRecursion(q, p % q);
        }
    """
        expect = """Program([
	FuncDecl(Id(gcdRecursion), IntegerType, [Param(Id(p), IntegerType), Param(Id(q), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(q), IntegerLit(0)), ReturnStmt(Id(p))), ReturnStmt(FuncCall(Id(gcdRecursion), [Id(q), BinExpr(%, Id(p), Id(q))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = """
        recursiveSearch: function integer(out n: integer, m: integer, arr: array[100] of integer, index: integer) {
          index = index + 1;
          if (index > n) {
            return -1;
          }

          if (arr[index - 1] == m) {
            for (i = index - 1, i < n - 1, i+1) {
              arr[i] = arr[i + 1];
            }
            n = n - 1;
            return index - 1;
          }
          return recursiveSearch(n, m, arr, index);
        }
    """
        expect = """Program([
	FuncDecl(Id(recursiveSearch), IntegerType, [OutParam(Id(n), IntegerType), Param(Id(m), IntegerType), Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(index), IntegerType)], None, BlockStmt([AssignStmt(Id(index), BinExpr(+, Id(index), IntegerLit(1))), IfStmt(BinExpr(>, Id(index), Id(n)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(==, ArrayCell(Id(arr), [BinExpr(-, Id(index), IntegerLit(1))]), Id(m)), BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, Id(index), IntegerLit(1))), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [BinExpr(+, Id(i), IntegerLit(1))]))])), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), ReturnStmt(BinExpr(-, Id(index), IntegerLit(1)))])), ReturnStmt(FuncCall(Id(recursiveSearch), [Id(n), Id(m), Id(arr), Id(index)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43(self):
        input = """
        isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (i = 0, i < size / 2, i+1) {
            if (head[i] != tail[i])
              return false;
          }
          return true;
        }
    """
        expect = """Program([
	FuncDecl(Id(isSymmetry), BooleanType, [Param(Id(head), ArrayType([100], IntegerType)), Param(Id(tail), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(size), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(Id(head), [Id(i)]), ArrayCell(Id(tail), [Id(i)])), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44(self):
        input = """
        countWaysUtil: function integer(x: integer, num: integer) {
          val: integer = (x - num*num);
          if (val == 0)
            return 1;
          if (val < 0)
            return 0;

          return countWaysUtil(val, num + 1) + countWaysUtil(x, num + 1);
        }
    """
        expect = """Program([
	FuncDecl(Id(countWaysUtil), IntegerType, [Param(Id(x), IntegerType), Param(Id(num), IntegerType)], None, BlockStmt([VarDecl(Id(val), IntegerType, BinExpr(-, Id(x), BinExpr(*, Id(num), Id(num)))), IfStmt(BinExpr(==, Id(val), IntegerLit(0)), ReturnStmt(IntegerLit(1))), IfStmt(BinExpr(<, Id(val), IntegerLit(0)), ReturnStmt(IntegerLit(0))), ReturnStmt(BinExpr(+, FuncCall(Id(countWaysUtil), [Id(val), BinExpr(+, Id(num), IntegerLit(1))]), FuncCall(Id(countWaysUtil), [Id(x), BinExpr(+, Id(num), IntegerLit(1))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    # # # Test mix # # #
    def test_45(self):
        input = """
        a, b, c : integer = -1, 0, 3;
        y, z : integer = 1, 1;
        x : array [0, 100] of integer;
        main: function void() {
            for (i = 0, i < 100, i+1) {
                a = b + c;
                x[0, i] = y % z;
            }
        }
    """
        expect = """Program([
	VarDecl(Id(a), IntegerType, UnExpr(-, IntegerLit(1)))
	VarDecl(Id(b), IntegerType, IntegerLit(0))
	VarDecl(Id(c), IntegerType, IntegerLit(3))
	VarDecl(Id(y), IntegerType, IntegerLit(1))
	VarDecl(Id(z), IntegerType, IntegerLit(1))
	VarDecl(Id(x), ArrayType([0, 100], IntegerType))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(b), Id(c))), AssignStmt(ArrayCell(Id(x), [IntegerLit(0), Id(i)]), BinExpr(%, Id(y), Id(z)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT: function integer(i: integer) { return (2 * i + 1); }

        RIGHT: function integer(i: integer) { return (2 * i + 2); }
    """
        expect = """Program([
	FuncDecl(Id(PARENT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(-, Id(i), IntegerLit(1)), IntegerLit(2)))]))
	FuncDecl(Id(LEFT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(1)))]))
	FuncDecl(Id(RIGHT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT: function integer(i: integer) { return (2 * i + 1); }

        RIGHT: function integer(i: integer) { return (2 * i + 2); }

        reheapUp: function void (maxHeap: array [100] of integer, numberOfElements: integer, index: integer)
        {
            if (index >= numberOfElements) {
                return;
            }
            if (index && maxHeap[PARENT(index)] < maxHeap[index]) {
                temp: integer = maxHeap[index];
                maxHeap[index] = maxHeap[PARENT(index)];
                maxHeap[PARENT(index)] = temp;
                reheapUp(maxHeap, numberOfElements, PARENT(index));
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(PARENT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(-, Id(i), IntegerLit(1)), IntegerLit(2)))]))
	FuncDecl(Id(LEFT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(1)))]))
	FuncDecl(Id(RIGHT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(2)))]))
	FuncDecl(Id(reheapUp), VoidType, [Param(Id(maxHeap), ArrayType([100], IntegerType)), Param(Id(numberOfElements), IntegerType), Param(Id(index), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(index), Id(numberOfElements)), BlockStmt([ReturnStmt()])), IfStmt(BinExpr(<, BinExpr(&&, Id(index), ArrayCell(Id(maxHeap), [FuncCall(Id(PARENT), [Id(index)])])), ArrayCell(Id(maxHeap), [Id(index)])), BlockStmt([VarDecl(Id(temp), IntegerType, ArrayCell(Id(maxHeap), [Id(index)])), AssignStmt(ArrayCell(Id(maxHeap), [Id(index)]), ArrayCell(Id(maxHeap), [FuncCall(Id(PARENT), [Id(index)])])), AssignStmt(ArrayCell(Id(maxHeap), [FuncCall(Id(PARENT), [Id(index)])]), Id(temp)), CallStmt(Id(reheapUp), Id(maxHeap), Id(numberOfElements), FuncCall(Id(PARENT), [Id(index)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_48(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT: function integer(i: integer) { return (2 * i + 1); }

        RIGHT: function integer(i: integer) { return (2 * i + 2); }

        reheapDown: function void(maxHeap: array [100] of integer, numberOfElements: integer, index: integer)
        {
            if (index >= numberOfElements) {
                return;
            }
                left: integer = LEFT(index);
                right: integer = RIGHT(index);
         
                largest: integer = index;
         
                if (left < numberOfElements && (maxHeap[left] > maxHeap[index])) {
                    largest = left;
                }
         
                if (right < numberOfElements && (maxHeap[right] > maxHeap[largest])) {
                    largest = right;
                }
         
                if (largest != index)
                {
                    temp:integer  = maxHeap[index];
                    maxHeap[index] = maxHeap[largest];
                    maxHeap[largest] = temp;
                    reheapDown(maxHeap, numberOfElements, largest);
                }
        }
    """
        expect = """Program([
	FuncDecl(Id(PARENT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(-, Id(i), IntegerLit(1)), IntegerLit(2)))]))
	FuncDecl(Id(LEFT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(1)))]))
	FuncDecl(Id(RIGHT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(2)))]))
	FuncDecl(Id(reheapDown), VoidType, [Param(Id(maxHeap), ArrayType([100], IntegerType)), Param(Id(numberOfElements), IntegerType), Param(Id(index), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(index), Id(numberOfElements)), BlockStmt([ReturnStmt()])), VarDecl(Id(left), IntegerType, FuncCall(Id(LEFT), [Id(index)])), VarDecl(Id(right), IntegerType, FuncCall(Id(RIGHT), [Id(index)])), VarDecl(Id(largest), IntegerType, Id(index)), IfStmt(BinExpr(<, Id(left), BinExpr(&&, Id(numberOfElements), BinExpr(>, ArrayCell(Id(maxHeap), [Id(left)]), ArrayCell(Id(maxHeap), [Id(index)])))), BlockStmt([AssignStmt(Id(largest), Id(left))])), IfStmt(BinExpr(<, Id(right), BinExpr(&&, Id(numberOfElements), BinExpr(>, ArrayCell(Id(maxHeap), [Id(right)]), ArrayCell(Id(maxHeap), [Id(largest)])))), BlockStmt([AssignStmt(Id(largest), Id(right))])), IfStmt(BinExpr(!=, Id(largest), Id(index)), BlockStmt([VarDecl(Id(temp), IntegerType, ArrayCell(Id(maxHeap), [Id(index)])), AssignStmt(ArrayCell(Id(maxHeap), [Id(index)]), ArrayCell(Id(maxHeap), [Id(largest)])), AssignStmt(ArrayCell(Id(maxHeap), [Id(largest)]), Id(temp)), CallStmt(Id(reheapDown), Id(maxHeap), Id(numberOfElements), Id(largest))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
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
    """
        expect = """Program([
	VarDecl(Id(less_zero), BooleanType, BooleanLit(False))
	VarDecl(Id(c), IntegerType, IntegerLit(0))
	FuncDecl(Id(printegerPattern), VoidType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(less_zero), BooleanLit(False))])), IfStmt(Id(less_zero), BlockStmt([AssignStmt(Id(c), BinExpr(-, Id(c), IntegerLit(1))), IfStmt(BinExpr(==, Id(c), UnExpr(-, IntegerLit(1))), ReturnStmt()), CallStmt(Id(printegerPattern), BinExpr(+, Id(n), IntegerLit(5)))]), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1))), CallStmt(Id(printegerPattern), BinExpr(-, Id(n), IntegerLit(5)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
        input = """
        buildMaxHeap: function void(arr: array[100] of integer, numOfEl: integer) {
            for (i = numOfEl / 2 - 1, i >= 0, i-1) {
              heapify(arr, numOfEl, i);
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(buildMaxHeap), VoidType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(/, Id(numOfEl), IntegerLit(2)), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(Id(heapify), Id(arr), Id(numOfEl), Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = """
        moduloDivision: function integer(seed: integer, mod: integer) { return seed % mod; }
    """
        expect = """Program([
	FuncDecl(Id(moduloDivision), IntegerType, [Param(Id(seed), IntegerType), Param(Id(mod), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(%, Id(seed), Id(mod)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52(self):
        input = """
        binarySearch: function integer(arr: array[1000] of integer, left: integer, right: integer, x: integer) {
          if (right >= left) {
            mid:integer = left + (right - left) / 2;
            if (arr[mid] == x)
              return mid;

            if (arr[mid] > x)
              return binarySearch(arr, left, mid - 1, x);

            return binarySearch(arr, mid + 1, right, x);
          }

          return -1;
        }
    """
        expect = """Program([
	FuncDecl(Id(binarySearch), IntegerType, [Param(Id(arr), ArrayType([1000], IntegerType)), Param(Id(left), IntegerType), Param(Id(right), IntegerType), Param(Id(x), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(right), Id(left)), BlockStmt([VarDecl(Id(mid), IntegerType, BinExpr(+, Id(left), BinExpr(/, BinExpr(-, Id(right), Id(left)), IntegerLit(2)))), IfStmt(BinExpr(==, ArrayCell(Id(arr), [Id(mid)]), Id(x)), ReturnStmt(Id(mid))), IfStmt(BinExpr(>, ArrayCell(Id(arr), [Id(mid)]), Id(x)), ReturnStmt(FuncCall(Id(binarySearch), [Id(arr), Id(left), BinExpr(-, Id(mid), IntegerLit(1)), Id(x)]))), ReturnStmt(FuncCall(Id(binarySearch), [Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(right), Id(x)]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

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
            printegerIntegereger(x);
        }
    """
        expect = """Program([
	VarDecl(Id(x), IntegerType, IntegerLit(65))
	FuncDecl(Id(fact), IntegerType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(Id(fact), [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(Id(inc), VoidType, [OutParam(Id(n), IntegerType), Param(Id(delta), IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(delta), IntegerType, FuncCall(Id(fact), [IntegerLit(3)])), CallStmt(Id(inc), Id(x), Id(delta)), CallStmt(Id(printegerIntegereger), Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54(self):
        input = """
        heapSort: function void (start: array[100] of integer, end: array[100] of integer, numOfEl: integer) {
            buildMaxHeap(start, numOfEl);
            for (i = numOfEl - 1, i >= 0, i-1) {
              temp: integer = start[0];
              start[0] = start[i];
              start[i] = temp;
              heapify(start, i, 0);
            }
            printArray(start, end);
          }
    """
        expect = """Program([
	FuncDecl(Id(heapSort), VoidType, [Param(Id(start), ArrayType([100], IntegerType)), Param(Id(end), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType)], None, BlockStmt([CallStmt(Id(buildMaxHeap), Id(start), Id(numOfEl)), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(numOfEl), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(temp), IntegerType, ArrayCell(Id(start), [IntegerLit(0)])), AssignStmt(ArrayCell(Id(start), [IntegerLit(0)]), ArrayCell(Id(start), [Id(i)])), AssignStmt(ArrayCell(Id(start), [Id(i)]), Id(temp)), CallStmt(Id(heapify), Id(start), Id(i), IntegerLit(0))])), CallStmt(Id(printArray), Id(start), Id(end))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_55(self):
        input = """
        heapify: function void(arr: array[100] of integer, numOfEl: integer, i: integer) {
            left, right, largest: integer = 2 * i + 1, 2 * i + 2, i;
            if ((left < numOfEl) && (arr[left] > arr[largest]))
              largest = left;
            if ((right < numOfEl) && (arr[right] > arr[largest]))
              largest = right;

            if (largest != i) {
              temp: integer = arr[i];
              arr[i] = arr[largest];
              arr[largest] = temp;
              heapify(arr, numOfEl, largest);
            }
          }
    """
        expect = """Program([
	FuncDecl(Id(heapify), VoidType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType), Param(Id(i), IntegerType)], None, BlockStmt([VarDecl(Id(left), IntegerType, BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(1))), VarDecl(Id(right), IntegerType, BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(2))), VarDecl(Id(largest), IntegerType, Id(i)), IfStmt(BinExpr(&&, BinExpr(<, Id(left), Id(numOfEl)), BinExpr(>, ArrayCell(Id(arr), [Id(left)]), ArrayCell(Id(arr), [Id(largest)]))), AssignStmt(Id(largest), Id(left))), IfStmt(BinExpr(&&, BinExpr(<, Id(right), Id(numOfEl)), BinExpr(>, ArrayCell(Id(arr), [Id(right)]), ArrayCell(Id(arr), [Id(largest)]))), AssignStmt(Id(largest), Id(right))), IfStmt(BinExpr(!=, Id(largest), Id(i)), BlockStmt([VarDecl(Id(temp), IntegerType, ArrayCell(Id(arr), [Id(i)])), AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(largest)])), AssignStmt(ArrayCell(Id(arr), [Id(largest)]), Id(temp)), CallStmt(Id(heapify), Id(arr), Id(numOfEl), Id(largest))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56(self):
        input = """
        min_waiting_time: function integer (n: integer, arrvalTime: array[100] of integer, completeTime: array[100] of integer) {
            sort(a, a + n, greater());
            minTime : integer = 0;
            for (i = 0, i < n, i + k)
                minTime = minTime + (2 * a[i]);
            return minTime;
        }
    """
        expect = """Program([
	FuncDecl(Id(min_waiting_time), IntegerType, [Param(Id(n), IntegerType), Param(Id(arrvalTime), ArrayType([100], IntegerType)), Param(Id(completeTime), ArrayType([100], IntegerType))], None, BlockStmt([CallStmt(Id(sort), Id(a), BinExpr(+, Id(a), Id(n)), FuncCall(Id(greater), [])), VarDecl(Id(minTime), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), Id(k)), AssignStmt(Id(minTime), BinExpr(+, Id(minTime), BinExpr(*, IntegerLit(2), ArrayCell(Id(a), [Id(i)]))))), ReturnStmt(Id(minTime))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57(self):
        input = """
        swap: function void(x: integer,y: integer) {
          k: integer = x;
          x = y;
          y = k;
        }
    """
        expect = """Program([
	FuncDecl(Id(swap), VoidType, [Param(Id(x), IntegerType), Param(Id(y), IntegerType)], None, BlockStmt([VarDecl(Id(k), IntegerType, Id(x)), AssignStmt(Id(x), Id(y)), AssignStmt(Id(y), Id(k))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58(self):
        input = """
        longestSublist: function integer (words: array[100] of string, size: integer) {
            if(!size) return 0;
            result : integer = 1;
            for (i = 0, i < size - 1, i + 1) {
                if (words[i, 0] == words[i + 1, 0]) {
                  pre_result, j: integer  = 2 , i + 1;
                  while (j < size - 1) {
                    if (words[j, 0] == words[j + 1, 0]) {
                      pre_result = pre_result + 1;
                      j = j + 1;
                    } else {
                      break;
                    }
                  }
                  if(pre_result > result) result = pre_result;
                }
            }
            return result;
        }
    """
        expect = """Program([
	FuncDecl(Id(longestSublist), IntegerType, [Param(Id(words), ArrayType([100], StringType)), Param(Id(size), IntegerType)], None, BlockStmt([IfStmt(UnExpr(!, Id(size)), ReturnStmt(IntegerLit(0))), VarDecl(Id(result), IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(size), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(words), [Id(i), IntegerLit(0)]), ArrayCell(Id(words), [BinExpr(+, Id(i), IntegerLit(1)), IntegerLit(0)])), BlockStmt([VarDecl(Id(pre_result), IntegerType, IntegerLit(2)), VarDecl(Id(j), IntegerType, BinExpr(+, Id(i), IntegerLit(1))), WhileStmt(BinExpr(<, Id(j), BinExpr(-, Id(size), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(words), [Id(j), IntegerLit(0)]), ArrayCell(Id(words), [BinExpr(+, Id(j), IntegerLit(1)), IntegerLit(0)])), BlockStmt([AssignStmt(Id(pre_result), BinExpr(+, Id(pre_result), IntegerLit(1))), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))]), BlockStmt([BreakStmt()]))])), IfStmt(BinExpr(>, Id(pre_result), Id(result)), AssignStmt(Id(result), Id(pre_result)))]))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_59(self):
        input = """
        test : function void () {
            nE : integer = 0;
            for (i = 0, i < nE, i + 1) 
                if (nE == 10 + 5) 
                    break;
        }
    """
        expect = """Program([
	FuncDecl(Id(test), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(nE)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(nE), BinExpr(+, IntegerLit(10), IntegerLit(5))), BreakStmt()))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60(self):
        input = """
        reverse_string: function string(str: string, size: integer) {
            for (i = 0, i < size / 2, i+1) {
                x : string = str[i];
                str[i] = str[size - i - 1];
                str[size - i - 1] = x;
            }
            return str;
        }
    """
        expect = """Program([
	FuncDecl(Id(reverse_string), StringType, [Param(Id(str), StringType), Param(Id(size), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(size), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(x), StringType, ArrayCell(Id(str), [Id(i)])), AssignStmt(ArrayCell(Id(str), [Id(i)]), ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(size), Id(i)), IntegerLit(1))])), AssignStmt(ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(size), Id(i)), IntegerLit(1))]), Id(x))])), ReturnStmt(Id(str))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61(self):
        input = """
        checkStrCode: function boolean (code : string, size: integer) {
            if (code == "")
                return false;
            for (i = 0, i < size, i + 6 - 3) {
                if (!(((code[i] >= "a") && (code[i] <= "z")) ||
                      ((code[i] >= "A") && (code[i] <= "Z")))) {
                    break;
                }
            }
            return true;
        }
    """
        expect = """Program([
	FuncDecl(Id(checkStrCode), BooleanType, [Param(Id(code), StringType), Param(Id(size), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(code), StringLit()), ReturnStmt(BooleanLit(False))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(size)), BinExpr(-, BinExpr(+, Id(i), IntegerLit(6)), IntegerLit(3)), BlockStmt([IfStmt(UnExpr(!, BinExpr(||, BinExpr(&&, BinExpr(>=, ArrayCell(Id(code), [Id(i)]), StringLit(a)), BinExpr(<=, ArrayCell(Id(code), [Id(i)]), StringLit(z))), BinExpr(&&, BinExpr(>=, ArrayCell(Id(code), [Id(i)]), StringLit(A)), BinExpr(<=, ArrayCell(Id(code), [Id(i)]), StringLit(Z))))), BlockStmt([BreakStmt()]))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62(self):
        input = """
        fibonacci: function integer(n: integer) {
            f0, f1, fn: auto = 0, 1, 1;
            if (n < 0) {
                return -1;
            }
            if (n == 0 || (n == 1)) {
                return n;
            } else {
                for (i = 2, i < n, i + 1) {
                  f0 = f1;
                  f1 = fn;
                  fn = f0 + f1;
                }
            }
            return fn;
        }
    """
        expect = """Program([
	FuncDecl(Id(fibonacci), IntegerType, [Param(Id(n), IntegerType)], None, BlockStmt([VarDecl(Id(f0), AutoType, IntegerLit(0)), VarDecl(Id(f1), AutoType, IntegerLit(1)), VarDecl(Id(fn), AutoType, IntegerLit(1)), IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(==, Id(n), BinExpr(||, IntegerLit(0), BinExpr(==, Id(n), IntegerLit(1)))), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(f0), Id(f1)), AssignStmt(Id(f1), Id(fn)), AssignStmt(Id(fn), BinExpr(+, Id(f0), Id(f1)))]))])), ReturnStmt(Id(fn))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63(self):
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
    """
        expect = """Program([
	FuncDecl(Id(numIsPrime), BooleanType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), ReturnStmt(BooleanLit(False))), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), FuncCall(Id(sqrt), [Id(n)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64(self):
        input = """
        x : integer = 65;
        main : function void () {
            arr : array [2, 3] of integer;
            if(numIsPrime(7)){
                arr[1, 2] = Fibonacci(10);
            }
        }
    """
        expect = """Program([
	VarDecl(Id(x), IntegerType, IntegerLit(65))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(arr), ArrayType([2, 3], IntegerType)), IfStmt(FuncCall(Id(numIsPrime), [IntegerLit(7)]), BlockStmt([AssignStmt(ArrayCell(Id(arr), [IntegerLit(1), IntegerLit(2)]), FuncCall(Id(Fibonacci), [IntegerLit(10)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_65(self):
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
    """
        expect = """Program([
	FuncDecl(Id(inc), VoidType, [OutParam(Id(n), IntegerType), Param(Id(delta), IntegerType)], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(0)), DoWhileStmt(BooleanLit(False), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(nE)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(nE), BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(Id(nE)), AssignStmt(Id(nE), BinExpr(+, Id(nE), IntegerLit(1))))), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_66(self):
        input = """
        increase : function void (out n: integer, delta : integer) {
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
    """
        expect = """Program([
	FuncDecl(Id(increase), VoidType, [OutParam(Id(n), IntegerType), Param(Id(delta), IntegerType)], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(0)), DoWhileStmt(BooleanLit(False), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(nE)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(nE), BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(Id(nE)), AssignStmt(Id(nE), BinExpr(+, Id(nE), IntegerLit(1))))), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_67(self):
        input = """
        midSquare: function integer (seed: integer) {
          newSeed: integer = pow(seed, 2);
          s: string = to_string(newSeed);
          erase(s, begin() + size(s) - 2, end(s));
          return stoi(substr(s, size(s) - 4));
        }
    """
        expect = """Program([
	FuncDecl(Id(midSquare), IntegerType, [Param(Id(seed), IntegerType)], None, BlockStmt([VarDecl(Id(newSeed), IntegerType, FuncCall(Id(pow), [Id(seed), IntegerLit(2)])), VarDecl(Id(s), StringType, FuncCall(Id(to_string), [Id(newSeed)])), CallStmt(Id(erase), Id(s), BinExpr(-, BinExpr(+, FuncCall(Id(begin), []), FuncCall(Id(size), [Id(s)])), IntegerLit(2)), FuncCall(Id(end), [Id(s)])), ReturnStmt(FuncCall(Id(stoi), [FuncCall(Id(substr), [Id(s), BinExpr(-, FuncCall(Id(size), [Id(s)]), IntegerLit(4))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68(self):
        input = """
        digitExtraction: function integer(seed: integer, extractDigits: array[100] of integer, size: integer) {
          s, strSeed: string = "", to_string(seed);
          for (i = 0, i < size, i+1) {
            s = s + strSeed[extractDigits[i]];
          }
          return stoi(s);
        }
    """
        expect = """Program([
	FuncDecl(Id(digitExtraction), IntegerType, [Param(Id(seed), IntegerType), Param(Id(extractDigits), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(s), StringType, StringLit()), VarDecl(Id(strSeed), StringType, FuncCall(Id(to_string), [Id(seed)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(size)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(s), ArrayCell(Id(strSeed), [ArrayCell(Id(extractDigits), [Id(i)])])))])), ReturnStmt(FuncCall(Id(stoi), [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69(self):
        input = """
        foldShift: function integer (key: integer, addressSize: integer) {
            x: string = to_string(key);
            sum: integer = 0;
          for (i = 0, i < length(x), i + 1) {
            s: string = substr(x, i, addressSize);
            i = i + addressSize;
            sum = sum + stoi(s);
          }
          test : integer = pow(10, addressSize);
          return sum % (test);
        }
    """
        expect = """Program([
	FuncDecl(Id(foldShift), IntegerType, [Param(Id(key), IntegerType), Param(Id(addressSize), IntegerType)], None, BlockStmt([VarDecl(Id(x), StringType, FuncCall(Id(to_string), [Id(key)])), VarDecl(Id(sum), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(Id(length), [Id(x)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(s), StringType, FuncCall(Id(substr), [Id(x), Id(i), Id(addressSize)])), AssignStmt(Id(i), BinExpr(+, Id(i), Id(addressSize))), AssignStmt(Id(sum), BinExpr(+, Id(sum), FuncCall(Id(stoi), [Id(s)])))])), VarDecl(Id(test), IntegerType, FuncCall(Id(pow), [IntegerLit(10), Id(addressSize)])), ReturnStmt(BinExpr(%, Id(sum), Id(test)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_70(self):
        input = """
        rotation: function integer (key: integer, addressSize: integer) {
          x: string = to_string(key);
          temp: string = x[length(x) - 1];
          for (i = length(x) - 1, i > 0, i-1) {
            x[i] = x[i - 1];
          }
          x[0] = temp;
          return foldShift(stoll(x), addressSize);
        }
    """
        expect = """Program([
	FuncDecl(Id(rotation), IntegerType, [Param(Id(key), IntegerType), Param(Id(addressSize), IntegerType)], None, BlockStmt([VarDecl(Id(x), StringType, FuncCall(Id(to_string), [Id(key)])), VarDecl(Id(temp), StringType, ArrayCell(Id(x), [BinExpr(-, FuncCall(Id(length), [Id(x)]), IntegerLit(1))])), ForStmt(AssignStmt(Id(i), BinExpr(-, FuncCall(Id(length), [Id(x)]), IntegerLit(1))), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(x), [Id(i)]), ArrayCell(Id(x), [BinExpr(-, Id(i), IntegerLit(1))]))])), AssignStmt(ArrayCell(Id(x), [IntegerLit(0)]), Id(temp)), ReturnStmt(FuncCall(Id(foldShift), [FuncCall(Id(stoll), [Id(x)]), Id(addressSize)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_71(self):
        input = """
        minStr: function string (S1: string , S2: string, sizeS1: integer, sizeS2: integer) {
          result : string = "";
          for (i = 0, i <= sizeS2 - sizeS1, i + 1) {
            result = S1::S2;
            if (containStr(S1, result)) {
              return result;
            }
          }
          return "Not found";
        }
    """
        expect = """Program([
	FuncDecl(Id(minStr), StringType, [Param(Id(S1), StringType), Param(Id(S2), StringType), Param(Id(sizeS1), IntegerType), Param(Id(sizeS2), IntegerType)], None, BlockStmt([VarDecl(Id(result), StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), BinExpr(-, Id(sizeS2), Id(sizeS1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(::, Id(S1), Id(S2))), IfStmt(FuncCall(Id(containStr), [Id(S1), Id(result)]), BlockStmt([ReturnStmt(Id(result))]))])), ReturnStmt(StringLit(Not found))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_72(self):
        input = """
        minStr: function string (S1: string , S2: string, sizeS1: integer, sizeS2: integer) {
          result : string = "";
          /*for (i = 0, i <= sizeS2 - sizeS1, i + 1) {
            result = S1::S2;
            if (containStr(S1, result)) {
              return result;
            }
          }*/
          return "Not found";
        }
    """
        expect = """Program([
	FuncDecl(Id(minStr), StringType, [Param(Id(S1), StringType), Param(Id(S2), StringType), Param(Id(sizeS1), IntegerType), Param(Id(sizeS2), IntegerType)], None, BlockStmt([VarDecl(Id(result), StringType, StringLit()), ReturnStmt(StringLit(Not found))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_73(self):
        input = """
        main : function void () {
            nE : integer = 0;
            for (i = 0, i < nE, i + 1) 
                if (nE == (10 + 5)) 
                    return nE;
                else i = i + 1;
        }
    """
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(nE)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(nE), BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(Id(nE)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74(self):
        input = """
        checkzero: function boolean(nums: array[100] of integer, size: integer) {}
        main : function void () {
            nE : integer = 100;
            nums: array[100] of integer = {1, 2, 3, 4};
            checkzero(nums, nE);
        }
    """
        expect = """Program([
	FuncDecl(Id(checkzero), BooleanType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(100)), VarDecl(Id(nums), ArrayType([100], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(Id(checkzero), Id(nums), Id(nE))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_75(self):
        input = """
        checkzero: function boolean(nums: array[100] of integer, size: integer) {}
        recursive: function void (nums: array[100] of integer, size: integer, index: integer , count: integer, sum: integer , minjump: integer) {}
        main : function void () {
            nE : integer = 100;
            nums: array[100] of integer = {1, 2, 3, 4};
            // checkzero(nums, nE);
            recursive(nums, 0, 0, 0, 1);
        }
    """
        expect = """Program([
	FuncDecl(Id(checkzero), BooleanType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(recursive), VoidType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType), Param(Id(index), IntegerType), Param(Id(count), IntegerType), Param(Id(sum), IntegerType), Param(Id(minjump), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(100)), VarDecl(Id(nums), ArrayType([100], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(Id(recursive), Id(nums), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
        input = """
        /* checkzero: function boolean(nums: array[100] of integer, size: integer) {}
         recursive: function void (nums: array[100] of integer, size: integer, index: integer , count: integer, sum: integer , minjump: integer) {} */
        jump: function integer(nums: array[100] of integer, size: integer) {}
        main : function void () {
            nE : integer = 100;
            nums: array[100] of integer = {1, 2, 3, 4};
            /* checkzero(nums, nE);
            recursive(nums, 0, 0, 0, 1); */
            jump(nums, 100);
        }
    """
        expect = """Program([
	FuncDecl(Id(jump), IntegerType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(100)), VarDecl(Id(nums), ArrayType([100], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(Id(jump), Id(nums), IntegerLit(100))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_77(self):
        input = """
        reverseStr: function string(str: string, size: integer) {}
        main : function void () {
            s : string = "Hello World!";
            reverseStr(s, 12);
        }
    """
        expect = """Program([
	FuncDecl(Id(reverseStr), StringType, [Param(Id(str), StringType), Param(Id(size), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(s), StringType, StringLit(Hello World!)), CallStmt(Id(reverseStr), Id(s), IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_78(self):
        input = """
        lengthOfLastWord: function integer(s: array[100] of string, size: integer) {}
        main : function void () {
            s : array[100] of string = {"Hello World!", "s1", "s2"};
            lengthOfLastWord(s, 100);
        }
    """
        expect = """Program([
	FuncDecl(Id(lengthOfLastWord), IntegerType, [Param(Id(s), ArrayType([100], StringType)), Param(Id(size), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(s), ArrayType([100], StringType), ArrayLit([StringLit(Hello World!), StringLit(s1), StringLit(s2)])), CallStmt(Id(lengthOfLastWord), Id(s), IntegerLit(100))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_79(self):
        input = """
        containStr: function boolean (S1: string , S2: string, sizeS1: integer, sizeS2: integer) {}
        main : function void () {
            S1, S2: string = "OKOK", "okok";
            lengthOfLastWord(S1, S2, 4, 4);
        }
    """
        expect = """Program([
	FuncDecl(Id(containStr), BooleanType, [Param(Id(S1), StringType), Param(Id(S2), StringType), Param(Id(sizeS1), IntegerType), Param(Id(sizeS2), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(S1), StringType, StringLit(OKOK)), VarDecl(Id(S2), StringType, StringLit(okok)), CallStmt(Id(lengthOfLastWord), Id(S1), Id(S2), IntegerLit(4), IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80(self):
        input = """
        search: function integer(nums: array[100] of integer, size: integer, target: integer) {}
        main : function void () {
            nE, target : integer = 100, 20;
            nums: array[100] of integer = {1, 2, 3, 4};
            search(nums, nE, target);
        }
    """
        expect = """Program([
	FuncDecl(Id(search), IntegerType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType), Param(Id(target), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(100)), VarDecl(Id(target), IntegerType, IntegerLit(20)), VarDecl(Id(nums), ArrayType([100], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(Id(search), Id(nums), Id(nE), Id(target))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_81(self):
        input = """
        // search: function integer(nums: array[100] of integer, size: integer, target: integer) {}
        completeNum: function boolean(N: integer) {}
        main : function void () {
            /* nE, target : integer = 100, 20;
            nums: array[100] of integer = {1, 2, 3, 4};
            search(nums, nE, target); */
            completeNum(10);
        }
    """
        expect = """Program([
	FuncDecl(Id(completeNum), BooleanType, [Param(Id(N), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(completeNum), IntegerLit(10))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_82(self):
        input = """
        max_two_nums: function auto (a: integer, b: integer) {}
        main : function void () {
            printInteger(max_two_nums(10, 20));
        }
    """
        expect = """Program([
	FuncDecl(Id(max_two_nums), AutoType, [Param(Id(a), IntegerType), Param(Id(b), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(printInteger), FuncCall(Id(max_two_nums), [IntegerLit(10), IntegerLit(20)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83(self):
        input = """
        min_two_nums: function auto (a: integer, b: integer) {}
        main : function void () {
            printInteger(min_two_nums(10, 20));
        }
    """
        expect = """Program([
	FuncDecl(Id(min_two_nums), AutoType, [Param(Id(a), IntegerType), Param(Id(b), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(printInteger), FuncCall(Id(min_two_nums), [IntegerLit(10), IntegerLit(20)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84(self):
        input = """
        factorial: function auto(N: integer) {}
        main : function void () {
            printFac(factorial(20));
        }
    """
        expect = """Program([
	FuncDecl(Id(factorial), AutoType, [Param(Id(N), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(printFac), FuncCall(Id(factorial), [IntegerLit(20)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85(self):
        input = """
        findMax: function auto(vals: array[100] of integer, numEls: integer) {}
        main : function void () {
            nE: integer = 100;
            nums: array[100] of integer = {100, 2, 3, 4};
            printMax(findMax(nums, nE));
        }
    """
        expect = """Program([
	FuncDecl(Id(findMax), AutoType, [Param(Id(vals), ArrayType([100], IntegerType)), Param(Id(numEls), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(100)), VarDecl(Id(nums), ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(Id(printMax), FuncCall(Id(findMax), [Id(nums), Id(nE)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86(self):
        input = """
        findMax: function auto(vals: array[100] of integer, numEls: integer) {}
        findMin: function auto(vals: array[100] of integer, numEls: integer) {}
        main : function void () {
            nE: integer = 100;
            nums: array[100] of integer = {100, 2, 3, 4};
            print(findMax(nums, nE));
            print(findMin(nums, nE));
        }
    """
        expect = """Program([
	FuncDecl(Id(findMax), AutoType, [Param(Id(vals), ArrayType([100], IntegerType)), Param(Id(numEls), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(findMin), AutoType, [Param(Id(vals), ArrayType([100], IntegerType)), Param(Id(numEls), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(100)), VarDecl(Id(nums), ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(Id(print), FuncCall(Id(findMax), [Id(nums), Id(nE)])), CallStmt(Id(print), FuncCall(Id(findMin), [Id(nums), Id(nE)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87(self):
        input = """
        findMax: function auto(vals: array[100] of integer, numEls: integer) {
          max: integer = vals[0];
          for (i = 1, i < numEls, i+1) {
            if (vals[i] > max) {
              max = vals[i];
            }
          }
          return max;
        }
        findMin: function auto(vals: array[100] of integer, numEls: integer) {
          min: integer = vals[0];
          for (i = 1, i < numEls, i+1) {
            if (vals[i] < min) {
              min = vals[i];
            }
          }
          return min;
        }
        main : function void () {
            nE: integer = 100;
            nums: array[100] of integer = {100, 2, 3, 4};
            print(findMax(nums, nE));
            print(findMin(nums, nE));
        }
    """
        expect = """Program([
	FuncDecl(Id(findMax), AutoType, [Param(Id(vals), ArrayType([100], IntegerType)), Param(Id(numEls), IntegerType)], None, BlockStmt([VarDecl(Id(max), IntegerType, ArrayCell(Id(vals), [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(numEls)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(Id(vals), [Id(i)]), Id(max)), BlockStmt([AssignStmt(Id(max), ArrayCell(Id(vals), [Id(i)]))]))])), ReturnStmt(Id(max))]))
	FuncDecl(Id(findMin), AutoType, [Param(Id(vals), ArrayType([100], IntegerType)), Param(Id(numEls), IntegerType)], None, BlockStmt([VarDecl(Id(min), IntegerType, ArrayCell(Id(vals), [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(numEls)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(Id(vals), [Id(i)]), Id(min)), BlockStmt([AssignStmt(Id(min), ArrayCell(Id(vals), [Id(i)]))]))])), ReturnStmt(Id(min))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(100)), VarDecl(Id(nums), ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(Id(print), FuncCall(Id(findMax), [Id(nums), Id(nE)])), CallStmt(Id(print), FuncCall(Id(findMin), [Id(nums), Id(nE)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_88(self):
        input = """
        isPalindrome: function boolean(str: array[100] of string, strSize: integer) {}
        main : function void () {
            str: array[100] of string= {"", "2", "23423", "23432"};
            nE: integer = 100;
            isPalindrome(str, nE);
        }
    """
        expect = """Program([
	FuncDecl(Id(isPalindrome), BooleanType, [Param(Id(str), ArrayType([100], StringType)), Param(Id(strSize), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(str), ArrayType([100], StringType), ArrayLit([StringLit(), StringLit(2), StringLit(23423), StringLit(23432)])), VarDecl(Id(nE), IntegerType, IntegerLit(100)), CallStmt(Id(isPalindrome), Id(str), Id(nE))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89(self):
        input = """
        checkElementsUniqueness: function boolean (arr: array[100] of integer, n: integer) {
            // some code here
        }
        main : function void () {
            nums: array[100] of integer = {100, 2, 3, 4};
            nE: integer = 100;
            if (checkElementsUniqueness(nums, nE) == true) {
                print("element is unique");
            } else {
                print("element is not unique");
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(checkElementsUniqueness), BooleanType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(n), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nums), ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), VarDecl(Id(nE), IntegerType, IntegerLit(100)), IfStmt(BinExpr(==, FuncCall(Id(checkElementsUniqueness), [Id(nums), Id(nE)]), BooleanLit(False)), BlockStmt([CallStmt(Id(print), StringLit(element is unique))]), BlockStmt([CallStmt(Id(print), StringLit(element is not unique))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90(self):
        input = """
        checkDuplicate: function boolean(ar: array[100] of integer, size: integer) {}
        main : function void () {
            nums: array[100] of integer = {100, 2, 3, 4};
            nE: integer = 100;
            if (checkDuplicate(nums, nE) == true) {
                print("");
            } else {
                print("");
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(checkDuplicate), BooleanType, [Param(Id(ar), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nums), ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), VarDecl(Id(nE), IntegerType, IntegerLit(100)), IfStmt(BinExpr(==, FuncCall(Id(checkDuplicate), [Id(nums), Id(nE)]), BooleanLit(False)), BlockStmt([CallStmt(Id(print), StringLit())]), BlockStmt([CallStmt(Id(print), StringLit())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91(self):
        input = """
        gcdIteration: function integer(p: integer, q: integer) {}
        main : function void () {
            p, q: integer = 100, 200;
            print(gcdIteration(p, q));
        }
    """
        expect = """Program([
	FuncDecl(Id(gcdIteration), IntegerType, [Param(Id(p), IntegerType), Param(Id(q), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(p), IntegerType, IntegerLit(100)), VarDecl(Id(q), IntegerType, IntegerLit(200)), CallStmt(Id(print), FuncCall(Id(gcdIteration), [Id(p), Id(q)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92(self):
        input = """
        gcdRecursion: function integer(p: integer, q: integer) {
          if (q == 0)
            return p;
          return gcdRecursion(q, p % q);
        }
        main : function void () {
            p, q: integer = 100, 200;
            print(gcdRecursion(p, q));
        }
    """
        expect = """Program([
	FuncDecl(Id(gcdRecursion), IntegerType, [Param(Id(p), IntegerType), Param(Id(q), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(q), IntegerLit(0)), ReturnStmt(Id(p))), ReturnStmt(FuncCall(Id(gcdRecursion), [Id(q), BinExpr(%, Id(p), Id(q))]))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(p), IntegerType, IntegerLit(100)), VarDecl(Id(q), IntegerType, IntegerLit(200)), CallStmt(Id(print), FuncCall(Id(gcdRecursion), [Id(p), Id(q)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_93(self):
        input = """
        recursiveSearch: function integer(out n: integer, m: integer, arr: array[100] of integer, index: integer) {}
        main : function void () {
            n, m, index: integer = 0, 0, 0;
            arr: array[100] of integer = {100, 2, 3, 4};
            print(recursiveSearch(n, m, arr, index));
        }
    """
        expect = """Program([
	FuncDecl(Id(recursiveSearch), IntegerType, [OutParam(Id(n), IntegerType), Param(Id(m), IntegerType), Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(index), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(n), IntegerType, IntegerLit(0)), VarDecl(Id(m), IntegerType, IntegerLit(0)), VarDecl(Id(index), IntegerType, IntegerLit(0)), VarDecl(Id(arr), ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(Id(print), FuncCall(Id(recursiveSearch), [Id(n), Id(m), Id(arr), Id(index)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94(self):
        input = """
        isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {}
        main : function void () {
            size: integer = 100;
            head, tail: array[100] of integer = {100, 2, 3, 4}, {};
            if (isSymmetry(head, tail, size) == true) {
                print("array is symmetric");
            } else {
                print("array is not symmetric");
            }
        }
    """
        expect = """Program([
	FuncDecl(Id(isSymmetry), BooleanType, [Param(Id(head), ArrayType([100], IntegerType)), Param(Id(tail), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(size), IntegerType, IntegerLit(100)), VarDecl(Id(head), ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), VarDecl(Id(tail), ArrayType([100], IntegerType), ArrayLit([])), IfStmt(BinExpr(==, FuncCall(Id(isSymmetry), [Id(head), Id(tail), Id(size)]), BooleanLit(False)), BlockStmt([CallStmt(Id(print), StringLit(array is symmetric))]), BlockStmt([CallStmt(Id(print), StringLit(array is not symmetric))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_95(self):
        input = """
        PARENT: function integer(i: integer) {}

        LEFT: function integer(i: integer) {}

        RIGHT: function integer(i: integer) {}

        reheapUp: function void (maxHeap: array [100] of integer, numberOfElements: integer, index: integer) {}

        main : function void () {
            index: integer = 1;
            maxHeap: array[100] of integer = {100_1, 20, 30, 40};
            reheapUp(maxHeap, 100, index);
        }
    """
        expect = """Program([
	FuncDecl(Id(PARENT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(LEFT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(RIGHT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(reheapUp), VoidType, [Param(Id(maxHeap), ArrayType([100], IntegerType)), Param(Id(numberOfElements), IntegerType), Param(Id(index), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(index), IntegerType, IntegerLit(1)), VarDecl(Id(maxHeap), ArrayType([100], IntegerType), ArrayLit([IntegerLit(1001), IntegerLit(20), IntegerLit(30), IntegerLit(40)])), CallStmt(Id(reheapUp), Id(maxHeap), IntegerLit(100), Id(index))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_96(self):
        input = """
        PARENT: function integer(i: integer) {}

        LEFT: function integer(i: integer) {}

        RIGHT: function integer(i: integer) {}

        // reheapUp: function void (maxHeap: array [100] of integer, numberOfElements: integer, index: integer) {}

        reheapDown: function void(maxHeap: array [100] of integer, numberOfElements: integer, index: integer) {}
        main : function void () {
            index: integer = 1;
            maxHeap: array[100] of integer = {100_1, 20, 30, 40};
            // reheapUp(maxHeap, 100, index);
            reheapDown(maxHeap, 100, index);
        }
    """
        expect = """Program([
	FuncDecl(Id(PARENT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(LEFT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(RIGHT), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(reheapDown), VoidType, [Param(Id(maxHeap), ArrayType([100], IntegerType)), Param(Id(numberOfElements), IntegerType), Param(Id(index), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(index), IntegerType, IntegerLit(1)), VarDecl(Id(maxHeap), ArrayType([100], IntegerType), ArrayLit([IntegerLit(1001), IntegerLit(20), IntegerLit(30), IntegerLit(40)])), CallStmt(Id(reheapDown), Id(maxHeap), IntegerLit(100), Id(index))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97(self):
        input = """
        buildMaxHeap: function void(arr: array[100] of integer, numOfEl: integer) {}

        heapSort: function void (start: array[100] of integer, numOfEl: integer) {
            buildMaxHeap(start, numOfEl);
            // some code here
        }

        main : function void () {
            index: integer = 1;
            maxHeap: array[100] of integer = {100_1, 20, 30, 40};
            heapSort(maxHeap, 100);
            print(maxHeap);
        }
    """
        expect = """Program([
	FuncDecl(Id(buildMaxHeap), VoidType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(heapSort), VoidType, [Param(Id(start), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType)], None, BlockStmt([CallStmt(Id(buildMaxHeap), Id(start), Id(numOfEl))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(index), IntegerType, IntegerLit(1)), VarDecl(Id(maxHeap), ArrayType([100], IntegerType), ArrayLit([IntegerLit(1001), IntegerLit(20), IntegerLit(30), IntegerLit(40)])), CallStmt(Id(heapSort), Id(maxHeap), IntegerLit(100)), CallStmt(Id(print), Id(maxHeap))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98(self):
        input = """
        buildMaxHeap: function void(arr: array[100] of integer, numOfEl: integer) {}

        heapify: function void(arr: array[100] of integer, numOfEl: integer, i: integer) {}

        heapSort: function void (start: array[100] of integer, numOfEl: integer) {
            buildMaxHeap(start, numOfEl);
            buildMaxHeap(start, numOfEl);
            for (i = numOfEl - 1, i >= 0, i-1) {
              temp: integer = start[0];
              start[0] = start[i];
              start[i] = temp;
              heapify(start, i, 0);
            }
            printArray(start, end);
        }

        main : function void () {
            index: integer = 1;
            maxHeap: array[100] of integer = {100_1, 20, 30, 40};
            heapSort(maxHeap, 100);
        }
    """
        expect = """Program([
	FuncDecl(Id(buildMaxHeap), VoidType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(heapify), VoidType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType), Param(Id(i), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(heapSort), VoidType, [Param(Id(start), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType)], None, BlockStmt([CallStmt(Id(buildMaxHeap), Id(start), Id(numOfEl)), CallStmt(Id(buildMaxHeap), Id(start), Id(numOfEl)), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(numOfEl), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(temp), IntegerType, ArrayCell(Id(start), [IntegerLit(0)])), AssignStmt(ArrayCell(Id(start), [IntegerLit(0)]), ArrayCell(Id(start), [Id(i)])), AssignStmt(ArrayCell(Id(start), [Id(i)]), Id(temp)), CallStmt(Id(heapify), Id(start), Id(i), IntegerLit(0))])), CallStmt(Id(printArray), Id(start), Id(end))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(index), IntegerType, IntegerLit(1)), VarDecl(Id(maxHeap), ArrayType([100], IntegerType), ArrayLit([IntegerLit(1001), IntegerLit(20), IntegerLit(30), IntegerLit(40)])), CallStmt(Id(heapSort), Id(maxHeap), IntegerLit(100))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_99(self):
        input = """
        swap: function void(out x: integer, out y: integer) {
          k: integer = x;
          x = y;
          y = k;
        }

        main : function void () {
            x, y: integer = 1, 3;
            swap(x, y);
            print((x + y) + "");
        }
    """
        expect = """Program([
	FuncDecl(Id(swap), VoidType, [OutParam(Id(x), IntegerType), OutParam(Id(y), IntegerType)], None, BlockStmt([VarDecl(Id(k), IntegerType, Id(x)), AssignStmt(Id(x), Id(y)), AssignStmt(Id(y), Id(k))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(x), IntegerType, IntegerLit(1)), VarDecl(Id(y), IntegerType, IntegerLit(3)), CallStmt(Id(swap), Id(x), Id(y)), CallStmt(Id(print), BinExpr(+, BinExpr(+, Id(x), Id(y)), StringLit()))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_100(self):
        input = """
        rotation: function integer (key: integer, addressSize: integer) {}

        midSquare: function integer (seed: integer) {}

        digitExtraction: function integer(seed: integer, extractDigits: array[100] of integer, size: integer) {}

        foldShift: function integer (key: integer, addressSize: integer) {}

        main : function void () {
            print(midSquare(62323));
            print(foldShift(62323, 5));
        }
    """
        expect = """Program([
	FuncDecl(Id(rotation), IntegerType, [Param(Id(key), IntegerType), Param(Id(addressSize), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(midSquare), IntegerType, [Param(Id(seed), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(digitExtraction), IntegerType, [Param(Id(seed), IntegerType), Param(Id(extractDigits), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(foldShift), IntegerType, [Param(Id(key), IntegerType), Param(Id(addressSize), IntegerType)], None, BlockStmt([]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(print), FuncCall(Id(midSquare), [IntegerLit(62323)])), CallStmt(Id(print), FuncCall(Id(foldShift), [IntegerLit(62323), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
