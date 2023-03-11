import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # # # Test Variable Declarations # # #
    def test_1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_3(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b, c: auto = 1 , 2 , 3;
        d, e, f: string = "hello_d" , "hello_e", "hello_f" ;
        a, b, c: float = 2.000001, 3.0000001, 40_1.1;
        a, b, c: boolean = false, false, false;
"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, IntegerLit(2))
	VarDecl(c, AutoType, IntegerLit(3))
	VarDecl(d, StringType, StringLit(hello_d))
	VarDecl(e, StringType, StringLit(hello_e))
	VarDecl(f, StringType, StringLit(hello_f))
	VarDecl(a, FloatType, FloatLit(2.000001))
	VarDecl(b, FloatType, FloatLit(3.0000001))
	VarDecl(c, FloatType, FloatLit(401.1))
	VarDecl(a, BooleanType, BooleanLit(False))
	VarDecl(b, BooleanType, BooleanLit(False))
	VarDecl(c, BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = """
        a, b, c: array [2, 3] of integer;
"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], IntegerType))
	VarDecl(b, ArrayType([2, 3], IntegerType))
	VarDecl(c, ArrayType([2, 3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6(self):
        input = """
        a, b, c: array [2, 3] of integer = {{1, 2, 3}, {0, 5, 6}}, {{}, {}}, {{2, 3}, {}};
"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(0), IntegerLit(5), IntegerLit(6)])]))
	VarDecl(b, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(c, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7(self):
        input = """
        a2, b2, c2   : array [2, 3] of float = {{1.33333, .5555e-1, 189.00000}, {157., 1_2_3_4., 1_2_3_56.1234}}, {{}, {}}, {{1.34, 12e8}, {}};
"""
        expect = """Program([
	VarDecl(a2, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.33333), FloatLit(.5555e-1), FloatLit(189.00000)]), ArrayLit([FloatLit(157.), FloatLit(1234.), FloatLit(12356.1234)])]))
	VarDecl(b2, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(c2, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.34), FloatLit(12e8)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input = """
        a, b, c : array [2, 3] of string = {{"x", "y"}, {"z"}}, {{}, {}}, {{"hello", "world"}, {"hihi"}};
"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(x), StringLit(y)]), ArrayLit([StringLit(z)])]))
	VarDecl(b, ArrayType([2, 3], StringType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(c, ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(hello), StringLit(world)]), ArrayLit([StringLit(hihi)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = """
        a, b, c : array [2] of boolean = {false, false}, {false}, {false};
"""
        expect = """Program([
	VarDecl(a, ArrayType([2], BooleanType), ArrayLit([BooleanLit(False), BooleanLit(False)]))
	VarDecl(b, ArrayType([2], BooleanType), ArrayLit([BooleanLit(False)]))
	VarDecl(c, ArrayType([2], BooleanType), ArrayLit([BooleanLit(False)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """
        a, b, c : integer = -1, 0, 3;
        y, z : integer = 1, 1;
        x : array [0, 100] of integer;
"""
        expect = """Program([
	VarDecl(a, IntegerType, UnExpr(-, IntegerLit(1)))
	VarDecl(b, IntegerType, IntegerLit(0))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(y, IntegerType, IntegerLit(1))
	VarDecl(z, IntegerType, IntegerLit(1))
	VarDecl(x, ArrayType([0, 100], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    # # # Test Function Declarations # # #
    def test_11(self):
        input = """main: function void () {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13(self):
        input = """
        main: function void() {
            found : boolean = false;
            is_Num, is_String: string = "", "";
            is_String = "TEST";
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(found, BooleanType, BooleanLit(False)), VarDecl(is_Num, StringType, StringLit()), VarDecl(is_String, StringType, StringLit()), AssignStmt(is_String, StringLit(TEST))]))
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
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, IntegerLit(100)), BinExpr(+, i, IntegerLit(1)), BlockStmt([CallStmt(foo, BinExpr(+, x, IntegerLit(1)), FuncCall(foo, [BinExpr(+, i, IntegerLit(1)), FuncCall(foo, [BinExpr(+, x, IntegerLit(2)), IntegerLit(1)])]))]))]))
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
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, IntegerLit(100)), BinExpr(+, i, IntegerLit(1)), BlockStmt([VarDecl(j, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, j, IntegerLit(200)), BlockStmt([AssignStmt(j, BinExpr(+, j, IntegerLit(1)))])), WhileStmt(BinExpr(!=, i, IntegerLit(20)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """
        main: function void(out x: array[0, 100] of integer) {}
    """
        expect = """Program([
	FuncDecl(main, VoidType, [OutParam(x, ArrayType([0, 100], IntegerType))], None, BlockStmt([]))
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
	FuncDecl(lengthOfFirstWord, AutoType, [], None, BlockStmt([ReturnStmt(StringLit())]))
	FuncDecl(lengthOfLastWord, AutoType, [], lengthOfFirstWord, BlockStmt([ReturnStmt(StringLit(lengthOfLastWord))]))
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
	FuncDecl(main, VoidType, [OutParam(x, ArrayType([0, 100], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, IntegerLit(100)), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, i, IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(x, [i, IntegerLit(0)]), i)]), BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(0), i]), BinExpr(+, i, IntegerLit(1)))]))]))]))
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
	FuncDecl(main, VoidType, [OutParam(x, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, IntegerLit(100)), BinExpr(+, i, IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(j, IntegerLit(1)), BinExpr(<, j, IntegerLit(200)), BinExpr(+, j, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, i, j), IntegerLit(2)), BlockStmt([CallStmt(foo, IntegerLit(2), BinExpr(+, x, IntegerLit(1)))]))]))]))]))
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
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, IntegerLit(100)), BinExpr(+, i, IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(j, IntegerLit(1)), BinExpr(<, j, IntegerLit(200)), BinExpr(+, j, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, i, j), IntegerLit(2)), BlockStmt([BreakStmt()]), BlockStmt([ContinueStmt()]))]))]))]))
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
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, IntegerLit(100)), BinExpr(+, i, IntegerLit(1)), BlockStmt([VarDecl(j, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, j, IntegerLit(200)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, i, j), IntegerLit(20)), BlockStmt([BreakStmt()]), BlockStmt([AssignStmt(j, BinExpr(+, j, IntegerLit(1)))]))]))]))]))
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
            return false;
          else
            return false;
        }
    """
        expect = """Program([
	FuncDecl(Check, BooleanType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([VarDecl(count, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, size), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(nums, [i]), IntegerLit(0)), AssignStmt(count, BinExpr(+, count, IntegerLit(1))))])), IfStmt(BinExpr(==, BinExpr(%, count, IntegerLit(2)), IntegerLit(0)), ReturnStmt(BooleanLit(False)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
        input = """
        checkzero: function boolean(nums: array[100] of integer, size: integer) {
          found: boolean = false;
          for (i = 0, i < size && !found, i + 1) {
            if (nums[i] == 0)
              found = false;
          }
          if (found)
            return false;
          else
            return false;
        }
    """
        expect = """Program([
	FuncDecl(checkzero, BooleanType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([VarDecl(found, BooleanType, BooleanLit(False)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(&&, size, UnExpr(!, found))), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(nums, [i]), IntegerLit(0)), AssignStmt(found, BooleanLit(False)))])), IfStmt(found, ReturnStmt(BooleanLit(False)), ReturnStmt(BooleanLit(False)))]))
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
	FuncDecl(Recursive, VoidType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType), Param(index, IntegerType), Param(count, IntegerType), Param(sum, IntegerType), Param(minjump, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, sum, size), BlockStmt([IfStmt(BinExpr(>, minjump, count), AssignStmt(minjump, count))]), BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<=, i, ArrayCell(nums, [index])), BinExpr(+, i, IntegerLit(1)), BlockStmt([CallStmt(Recursive, nums, BinExpr(+, index, i), BinExpr(+, count, IntegerLit(1)), BinExpr(+, sum, i), minjump)]))]))]))
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
	FuncDecl(jump, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([VarDecl(minjump, IntegerType, BinExpr(-, size, IntegerLit(1))), CallStmt(Recursive, nums, IntegerLit(0), IntegerLit(0), IntegerLit(0), minjump), ReturnStmt(minjump)]))
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
	FuncDecl(jump1, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([VarDecl(curend, IntegerType, IntegerLit(0)), VarDecl(curfarthest, IntegerType, IntegerLit(0)), VarDecl(jumps, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(-, size, IntegerLit(1))), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(curfarthest, FuncCall(max, [curfarthest, BinExpr(+, i, ArrayCell(nums, [i]))])), IfStmt(BinExpr(==, i, curend), BlockStmt([AssignStmt(curend, curfarthest), AssignStmt(jumps, BinExpr(+, jumps, IntegerLit(1)))]))])), ReturnStmt(jumps)]))
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
	FuncDecl(reverseStr, StringType, [Param(str, StringType), Param(size, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(/, size, IntegerLit(2))), BinExpr(+, i, IntegerLit(1)), BlockStmt([VarDecl(x, StringType, ArrayCell(str, [i])), AssignStmt(ArrayCell(str, [i]), ArrayCell(str, [BinExpr(-, BinExpr(-, size, i), IntegerLit(1))])), AssignStmt(ArrayCell(str, [BinExpr(-, BinExpr(-, size, i), IntegerLit(1))]), x)])), ReturnStmt(str)]))
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
	FuncDecl(lengthOfLastWord, IntegerType, [Param(s, ArrayType([100], StringType)), Param(size, IntegerType)], None, BlockStmt([VarDecl(count, IntegerType, IntegerLit(0)), IfStmt(BinExpr(==, size, IntegerLit(0)), ReturnStmt(IntegerLit(0))), VarDecl(i, IntegerType, BinExpr(-, size, IntegerLit(1))), WhileStmt(BinExpr(>=, BinExpr(&&, BinExpr(==, ArrayCell(s, [i]), StringLit( )), i), IntegerLit(0)), BlockStmt([AssignStmt(i, BinExpr(-, i, IntegerLit(1)))])), WhileStmt(BinExpr(!=, BinExpr(&&, BinExpr(>=, i, IntegerLit(0)), ArrayCell(s, [i])), StringLit( )), BlockStmt([AssignStmt(count, BinExpr(+, count, IntegerLit(1))), AssignStmt(i, BinExpr(-, i, IntegerLit(1)))])), ReturnStmt(count)]))
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
    """
        expect = """Program([
	FuncDecl(containStr, BooleanType, [Param(S1, StringType), Param(S2, StringType), Param(sizeS1, IntegerType), Param(sizeS2, IntegerType)], None, BlockStmt([VarDecl(b, ArrayType([1000], BooleanType)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, sizeS2), BinExpr(+, i, IntegerLit(1)), BlockStmt([VarDecl(found, BooleanType, BooleanLit(False)), ForStmt(AssignStmt(j, IntegerLit(0)), BinExpr(<, j, sizeS1), BinExpr(+, j, IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, ArrayCell(b, [j])), BlockStmt([IfStmt(BinExpr(==, ArrayCell(S2, [i]), ArrayCell(S1, [j])), BlockStmt([AssignStmt(found, BooleanLit(False)), AssignStmt(ArrayCell(b, [j]), BooleanLit(False))]))]))])), IfStmt(UnExpr(!, found), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(False))]))
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
    """
        expect = """Program([
	FuncDecl(search, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType), Param(target, IntegerType)], None, BlockStmt([VarDecl(left, IntegerType, IntegerLit(0)), VarDecl(right, IntegerType, BinExpr(-, size, IntegerLit(1))), VarDecl(index, IntegerType, UnExpr(-, IntegerLit(1))), VarDecl(found, BooleanType, BooleanLit(False)), WhileStmt(BinExpr(<=, left, BinExpr(&&, right, UnExpr(!, found))), BlockStmt([VarDecl(mid, IntegerType, BinExpr(/, BinExpr(+, left, right), IntegerLit(2))), IfStmt(BinExpr(==, ArrayCell(nums, [mid]), target), BlockStmt([AssignStmt(found, BooleanLit(False)), AssignStmt(index, mid)])), IfStmt(BinExpr(>=, ArrayCell(nums, [mid]), ArrayCell(nums, [left])), BlockStmt([IfStmt(BinExpr(>, ArrayCell(nums, [mid]), target), BlockStmt([IfStmt(BinExpr(<, target, ArrayCell(nums, [left])), AssignStmt(left, BinExpr(+, mid, IntegerLit(1))), AssignStmt(right, BinExpr(-, mid, IntegerLit(1))))]), AssignStmt(left, BinExpr(+, mid, IntegerLit(1))))]), BlockStmt([IfStmt(BinExpr(>, target, ArrayCell(nums, [mid])), BlockStmt([IfStmt(BinExpr(>, target, ArrayCell(nums, [right])), AssignStmt(right, BinExpr(-, mid, IntegerLit(1))), AssignStmt(left, BinExpr(+, mid, IntegerLit(1))))]), AssignStmt(right, BinExpr(-, mid, IntegerLit(1))))]))])), ReturnStmt(index)]))
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
            return false;
          }
          return false;
        }
    """
        expect = """Program([
	FuncDecl(completeNum, BooleanType, [Param(N, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, N), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, N, i), IntegerLit(0)), BlockStmt([AssignStmt(sum, BinExpr(+, sum, i))]))])), IfStmt(BinExpr(==, sum, N), BlockStmt([ReturnStmt(BooleanLit(False))])), ReturnStmt(BooleanLit(False))]))
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
	FuncDecl(max_two_nums, AutoType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, a, b), BlockStmt([ReturnStmt(a)])), ReturnStmt(b)]))
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
	FuncDecl(min_two_nums, AutoType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, a, b), BlockStmt([ReturnStmt(a)])), ReturnStmt(b)]))
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
	FuncDecl(factorial, AutoType, [Param(N, IntegerType)], None, BlockStmt([VarDecl(result, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<=, i, N), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(result, BinExpr(*, result, i))])), ReturnStmt(result)]))
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
	FuncDecl(findMax, AutoType, [Param(vals, ArrayType([100], IntegerType)), Param(numEls, IntegerType)], None, BlockStmt([VarDecl(max, IntegerType, ArrayCell(vals, [IntegerLit(0)])), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, numEls), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(vals, [i]), max), BlockStmt([AssignStmt(max, ArrayCell(vals, [i]))]))])), ReturnStmt(max)]))
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
	FuncDecl(findMin, AutoType, [Param(vals, ArrayType([100], IntegerType)), Param(numEls, IntegerType)], None, BlockStmt([VarDecl(min, IntegerType, ArrayCell(vals, [IntegerLit(0)])), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, numEls), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(vals, [i]), min), BlockStmt([AssignStmt(min, ArrayCell(vals, [i]))]))])), ReturnStmt(min)]))
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
          return false;
        }
    """
        expect = """Program([
	FuncDecl(isPalindrome, BooleanType, [Param(str, ArrayType([100], StringType)), Param(strSize, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(/, strSize, IntegerLit(2))), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(str, [i]), ArrayCell(str, [BinExpr(-, BinExpr(-, strSize, i), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(False))]))
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
          return false;
        }
    """
        expect = """Program([
	FuncDecl(checkElementsUniqueness, BooleanType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(>, n, IntegerLit(1000)), BinExpr(<, n, IntegerLit(0))), ReturnStmt(BooleanLit(False))), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(-, n, IntegerLit(1))), BinExpr(+, i, IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(j, BinExpr(+, i, IntegerLit(1))), BinExpr(<, j, n), BinExpr(+, j, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [i]), ArrayCell(arr, [j])), ReturnStmt(BooleanLit(False)))]))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39(self):
        input = """
        checkDuplicate: function boolean(ar: array[100] of integer, size: integer) {
          if (size <= 1)
            return false;
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
	FuncDecl(checkDuplicate, BooleanType, [Param(ar, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, size, IntegerLit(1)), ReturnStmt(BooleanLit(False))), VarDecl(less, ArrayType([1000], IntegerType)), VarDecl(greater, ArrayType([1000], IntegerType)), VarDecl(greater_size, IntegerType, IntegerLit(0)), VarDecl(less_size, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, size), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(ar, [i]), ArrayCell(ar, [IntegerLit(0)])), BlockStmt([ReturnStmt(BooleanLit(False))])), IfStmt(BinExpr(<, ArrayCell(ar, [i]), ArrayCell(ar, [IntegerLit(0)])), BlockStmt([AssignStmt(ArrayCell(less, [less_size]), ArrayCell(ar, [i])), AssignStmt(less_size, BinExpr(+, less_size, IntegerLit(1)))]), BlockStmt([AssignStmt(ArrayCell(greater, [greater_size]), ArrayCell(ar, [i])), AssignStmt(greater_size, BinExpr(+, greater_size, IntegerLit(1)))]))])), ReturnStmt(BinExpr(&&, FuncCall(checkDuplicate, [less, less_size]), FuncCall(checkDuplicate, [greater, greater_size])))]))
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
	FuncDecl(gcdIteration, IntegerType, [Param(p, IntegerType), Param(q, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(!=, BinExpr(*, p, q), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(>, p, q), BlockStmt([AssignStmt(p, BinExpr(%, p, q))]), BlockStmt([AssignStmt(q, BinExpr(%, q, p))]))])), ReturnStmt(BinExpr(+, p, q))]))
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
	FuncDecl(gcdRecursion, IntegerType, [Param(p, IntegerType), Param(q, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, q, IntegerLit(0)), ReturnStmt(p)), ReturnStmt(FuncCall(gcdRecursion, [q, BinExpr(%, p, q)]))]))
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
	FuncDecl(recursiveSearch, IntegerType, [OutParam(n, IntegerType), Param(m, IntegerType), Param(arr, ArrayType([100], IntegerType)), Param(index, IntegerType)], None, BlockStmt([AssignStmt(index, BinExpr(+, index, IntegerLit(1))), IfStmt(BinExpr(>, index, n), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(==, ArrayCell(arr, [BinExpr(-, index, IntegerLit(1))]), m), BlockStmt([ForStmt(AssignStmt(i, BinExpr(-, index, IntegerLit(1))), BinExpr(<, i, BinExpr(-, n, IntegerLit(1))), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [i]), ArrayCell(arr, [BinExpr(+, i, IntegerLit(1))]))])), AssignStmt(n, BinExpr(-, n, IntegerLit(1))), ReturnStmt(BinExpr(-, index, IntegerLit(1)))])), ReturnStmt(FuncCall(recursiveSearch, [n, m, arr, index]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43(self):
        input = """
        isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (i = 0, i < size / 2, i+1) {
            if (head[i] != tail[i])
              return false;
          }
          return false;
        }
    """
        expect = """Program([
	FuncDecl(isSymmetry, BooleanType, [Param(head, ArrayType([100], IntegerType)), Param(tail, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(/, size, IntegerLit(2))), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(head, [i]), ArrayCell(tail, [i])), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(False))]))
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
	FuncDecl(countWaysUtil, IntegerType, [Param(x, IntegerType), Param(num, IntegerType)], None, BlockStmt([VarDecl(val, IntegerType, BinExpr(-, x, BinExpr(*, num, num))), IfStmt(BinExpr(==, val, IntegerLit(0)), ReturnStmt(IntegerLit(1))), IfStmt(BinExpr(<, val, IntegerLit(0)), ReturnStmt(IntegerLit(0))), ReturnStmt(BinExpr(+, FuncCall(countWaysUtil, [val, BinExpr(+, num, IntegerLit(1))]), FuncCall(countWaysUtil, [x, BinExpr(+, num, IntegerLit(1))])))]))
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
	VarDecl(a, IntegerType, UnExpr(-, IntegerLit(1)))
	VarDecl(b, IntegerType, IntegerLit(0))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(y, IntegerType, IntegerLit(1))
	VarDecl(z, IntegerType, IntegerLit(1))
	VarDecl(x, ArrayType([0, 100], IntegerType))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, IntegerLit(100)), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(a, BinExpr(+, b, c)), AssignStmt(ArrayCell(x, [IntegerLit(0), i]), BinExpr(%, y, z))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT: function integer(i: integer) { return (2 * i + 1); }

        RIGHT: function integer(i: integer) { return (2 * i + 2); }
    """
        expect = """Program([
	FuncDecl(PARENT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(-, i, IntegerLit(1)), IntegerLit(2)))]))
	FuncDecl(LEFT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), i), IntegerLit(1)))]))
	FuncDecl(RIGHT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), i), IntegerLit(2)))]))
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
	FuncDecl(PARENT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(-, i, IntegerLit(1)), IntegerLit(2)))]))
	FuncDecl(LEFT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), i), IntegerLit(1)))]))
	FuncDecl(RIGHT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), i), IntegerLit(2)))]))
	FuncDecl(reheapUp, VoidType, [Param(maxHeap, ArrayType([100], IntegerType)), Param(numberOfElements, IntegerType), Param(index, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, index, numberOfElements), BlockStmt([ReturnStmt()])), IfStmt(BinExpr(<, BinExpr(&&, index, ArrayCell(maxHeap, [FuncCall(PARENT, [index])])), ArrayCell(maxHeap, [index])), BlockStmt([VarDecl(temp, IntegerType, ArrayCell(maxHeap, [index])), AssignStmt(ArrayCell(maxHeap, [index]), ArrayCell(maxHeap, [FuncCall(PARENT, [index])])), AssignStmt(ArrayCell(maxHeap, [FuncCall(PARENT, [index])]), temp), CallStmt(reheapUp, maxHeap, numberOfElements, FuncCall(PARENT, [index]))]))]))
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
	FuncDecl(PARENT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(-, i, IntegerLit(1)), IntegerLit(2)))]))
	FuncDecl(LEFT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), i), IntegerLit(1)))]))
	FuncDecl(RIGHT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), i), IntegerLit(2)))]))
	FuncDecl(reheapDown, VoidType, [Param(maxHeap, ArrayType([100], IntegerType)), Param(numberOfElements, IntegerType), Param(index, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, index, numberOfElements), BlockStmt([ReturnStmt()])), VarDecl(left, IntegerType, FuncCall(LEFT, [index])), VarDecl(right, IntegerType, FuncCall(RIGHT, [index])), VarDecl(largest, IntegerType, index), IfStmt(BinExpr(<, left, BinExpr(&&, numberOfElements, BinExpr(>, ArrayCell(maxHeap, [left]), ArrayCell(maxHeap, [index])))), BlockStmt([AssignStmt(largest, left)])), IfStmt(BinExpr(<, right, BinExpr(&&, numberOfElements, BinExpr(>, ArrayCell(maxHeap, [right]), ArrayCell(maxHeap, [largest])))), BlockStmt([AssignStmt(largest, right)])), IfStmt(BinExpr(!=, largest, index), BlockStmt([VarDecl(temp, IntegerType, ArrayCell(maxHeap, [index])), AssignStmt(ArrayCell(maxHeap, [index]), ArrayCell(maxHeap, [largest])), AssignStmt(ArrayCell(maxHeap, [largest]), temp), CallStmt(reheapDown, maxHeap, numberOfElements, largest)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
        input = """
        less_zero: boolean = false;
        c: integer = 0;

        printegerPattern: function void(n: integer) {
          if (n <= 0) {
            less_zero = false;
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
	VarDecl(less_zero, BooleanType, BooleanLit(False))
	VarDecl(c, IntegerType, IntegerLit(0))
	FuncDecl(printegerPattern, VoidType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, n, IntegerLit(0)), BlockStmt([AssignStmt(less_zero, BooleanLit(False))])), IfStmt(less_zero, BlockStmt([AssignStmt(c, BinExpr(-, c, IntegerLit(1))), IfStmt(BinExpr(==, c, UnExpr(-, IntegerLit(1))), ReturnStmt()), CallStmt(printegerPattern, BinExpr(+, n, IntegerLit(5)))]), BlockStmt([AssignStmt(c, BinExpr(+, c, IntegerLit(1))), CallStmt(printegerPattern, BinExpr(-, n, IntegerLit(5)))]))]))
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
	FuncDecl(buildMaxHeap, VoidType, [Param(arr, ArrayType([100], IntegerType)), Param(numOfEl, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(i, BinExpr(-, BinExpr(/, numOfEl, IntegerLit(2)), IntegerLit(1))), BinExpr(>=, i, IntegerLit(0)), BinExpr(-, i, IntegerLit(1)), BlockStmt([CallStmt(heapify, arr, numOfEl, i)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = """
        moduloDivision: function integer(seed: integer, mod: integer) { return seed % mod; }
    """
        expect = """Program([
	FuncDecl(moduloDivision, IntegerType, [Param(seed, IntegerType), Param(mod, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(%, seed, mod))]))
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
	FuncDecl(binarySearch, IntegerType, [Param(arr, ArrayType([1000], IntegerType)), Param(left, IntegerType), Param(right, IntegerType), Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, right, left), BlockStmt([VarDecl(mid, IntegerType, BinExpr(+, left, BinExpr(/, BinExpr(-, right, left), IntegerLit(2)))), IfStmt(BinExpr(==, ArrayCell(arr, [mid]), x), ReturnStmt(mid)), IfStmt(BinExpr(>, ArrayCell(arr, [mid]), x), ReturnStmt(FuncCall(binarySearch, [arr, left, BinExpr(-, mid, IntegerLit(1)), x]))), ReturnStmt(FuncCall(binarySearch, [arr, BinExpr(+, mid, IntegerLit(1)), right, x]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
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
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, n, IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, n, FuncCall(fact, [BinExpr(-, n, IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(n, BinExpr(+, n, delta))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, x, delta), CallStmt(printegerIntegereger, x)]))
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
	FuncDecl(heapSort, VoidType, [Param(start, ArrayType([100], IntegerType)), Param(end, ArrayType([100], IntegerType)), Param(numOfEl, IntegerType)], None, BlockStmt([CallStmt(buildMaxHeap, start, numOfEl), ForStmt(AssignStmt(i, BinExpr(-, numOfEl, IntegerLit(1))), BinExpr(>=, i, IntegerLit(0)), BinExpr(-, i, IntegerLit(1)), BlockStmt([VarDecl(temp, IntegerType, ArrayCell(start, [IntegerLit(0)])), AssignStmt(ArrayCell(start, [IntegerLit(0)]), ArrayCell(start, [i])), AssignStmt(ArrayCell(start, [i]), temp), CallStmt(heapify, start, i, IntegerLit(0))])), CallStmt(printArray, start, end)]))
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
	FuncDecl(heapify, VoidType, [Param(arr, ArrayType([100], IntegerType)), Param(numOfEl, IntegerType), Param(i, IntegerType)], None, BlockStmt([VarDecl(left, IntegerType, BinExpr(+, BinExpr(*, IntegerLit(2), i), IntegerLit(1))), VarDecl(right, IntegerType, BinExpr(+, BinExpr(*, IntegerLit(2), i), IntegerLit(2))), VarDecl(largest, IntegerType, i), IfStmt(BinExpr(&&, BinExpr(<, left, numOfEl), BinExpr(>, ArrayCell(arr, [left]), ArrayCell(arr, [largest]))), AssignStmt(largest, left)), IfStmt(BinExpr(&&, BinExpr(<, right, numOfEl), BinExpr(>, ArrayCell(arr, [right]), ArrayCell(arr, [largest]))), AssignStmt(largest, right)), IfStmt(BinExpr(!=, largest, i), BlockStmt([VarDecl(temp, IntegerType, ArrayCell(arr, [i])), AssignStmt(ArrayCell(arr, [i]), ArrayCell(arr, [largest])), AssignStmt(ArrayCell(arr, [largest]), temp), CallStmt(heapify, arr, numOfEl, largest)]))]))
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
	FuncDecl(min_waiting_time, IntegerType, [Param(n, IntegerType), Param(arrvalTime, ArrayType([100], IntegerType)), Param(completeTime, ArrayType([100], IntegerType))], None, BlockStmt([CallStmt(sort, a, BinExpr(+, a, n), FuncCall(greater, [])), VarDecl(minTime, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, n), BinExpr(+, i, k), AssignStmt(minTime, BinExpr(+, minTime, BinExpr(*, IntegerLit(2), ArrayCell(a, [i]))))), ReturnStmt(minTime)]))
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
	FuncDecl(swap, VoidType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([VarDecl(k, IntegerType, x), AssignStmt(x, y), AssignStmt(y, k)]))
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
	FuncDecl(longestSublist, IntegerType, [Param(words, ArrayType([100], StringType)), Param(size, IntegerType)], None, BlockStmt([IfStmt(UnExpr(!, size), ReturnStmt(IntegerLit(0))), VarDecl(result, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(-, size, IntegerLit(1))), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(words, [i, IntegerLit(0)]), ArrayCell(words, [BinExpr(+, i, IntegerLit(1)), IntegerLit(0)])), BlockStmt([VarDecl(pre_result, IntegerType, IntegerLit(2)), VarDecl(j, IntegerType, BinExpr(+, i, IntegerLit(1))), WhileStmt(BinExpr(<, j, BinExpr(-, size, IntegerLit(1))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(words, [j, IntegerLit(0)]), ArrayCell(words, [BinExpr(+, j, IntegerLit(1)), IntegerLit(0)])), BlockStmt([AssignStmt(pre_result, BinExpr(+, pre_result, IntegerLit(1))), AssignStmt(j, BinExpr(+, j, IntegerLit(1)))]), BlockStmt([BreakStmt()]))])), IfStmt(BinExpr(>, pre_result, result), AssignStmt(result, pre_result))]))])), ReturnStmt(result)]))
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
	FuncDecl(test, VoidType, [], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, nE), BinExpr(+, i, IntegerLit(1)), IfStmt(BinExpr(==, nE, BinExpr(+, IntegerLit(10), IntegerLit(5))), BreakStmt()))]))
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
	FuncDecl(reverse_string, StringType, [Param(str, StringType), Param(size, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(/, size, IntegerLit(2))), BinExpr(+, i, IntegerLit(1)), BlockStmt([VarDecl(x, StringType, ArrayCell(str, [i])), AssignStmt(ArrayCell(str, [i]), ArrayCell(str, [BinExpr(-, BinExpr(-, size, i), IntegerLit(1))])), AssignStmt(ArrayCell(str, [BinExpr(-, BinExpr(-, size, i), IntegerLit(1))]), x)])), ReturnStmt(str)]))
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
            return false;
        }
    """
        expect = """Program([
	FuncDecl(checkStrCode, BooleanType, [Param(code, StringType), Param(size, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, code, StringLit()), ReturnStmt(BooleanLit(False))), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, size), BinExpr(-, BinExpr(+, i, IntegerLit(6)), IntegerLit(3)), BlockStmt([IfStmt(UnExpr(!, BinExpr(||, BinExpr(&&, BinExpr(>=, ArrayCell(code, [i]), StringLit(a)), BinExpr(<=, ArrayCell(code, [i]), StringLit(z))), BinExpr(&&, BinExpr(>=, ArrayCell(code, [i]), StringLit(A)), BinExpr(<=, ArrayCell(code, [i]), StringLit(Z))))), BlockStmt([BreakStmt()]))])), ReturnStmt(BooleanLit(False))]))
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
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(f0, AutoType, IntegerLit(0)), VarDecl(f1, AutoType, IntegerLit(1)), VarDecl(fn, AutoType, IntegerLit(1)), IfStmt(BinExpr(<, n, IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(==, n, BinExpr(||, IntegerLit(0), BinExpr(==, n, IntegerLit(1)))), BlockStmt([ReturnStmt(n)]), BlockStmt([ForStmt(AssignStmt(i, IntegerLit(2)), BinExpr(<, i, n), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(f0, f1), AssignStmt(f1, fn), AssignStmt(fn, BinExpr(+, f0, f1))]))])), ReturnStmt(fn)]))
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
          return false;
        }
    """
        expect = """Program([
	FuncDecl(numIsPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, n, IntegerLit(2)), ReturnStmt(BooleanLit(False))), ForStmt(AssignStmt(i, IntegerLit(2)), BinExpr(<=, i, FuncCall(sqrt, [n])), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, n, i), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(False))]))
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
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([2, 3], IntegerType)), IfStmt(FuncCall(numIsPrime, [IntegerLit(7)]), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(1), IntegerLit(2)]), FuncCall(Fibonacci, [IntegerLit(10)]))]))]))
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
            } while(false);
        }
    """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(0)), DoWhileStmt(BooleanLit(False), BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, nE), BinExpr(+, i, IntegerLit(1)), IfStmt(BinExpr(==, nE, BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(nE), AssignStmt(nE, BinExpr(+, nE, IntegerLit(1))))), ContinueStmt()]))]))
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
            } while(false);
        }
    """
        expect = """Program([
	FuncDecl(increase, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(0)), DoWhileStmt(BooleanLit(False), BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, nE), BinExpr(+, i, IntegerLit(1)), IfStmt(BinExpr(==, nE, BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(nE), AssignStmt(nE, BinExpr(+, nE, IntegerLit(1))))), ContinueStmt()]))]))
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
	FuncDecl(midSquare, IntegerType, [Param(seed, IntegerType)], None, BlockStmt([VarDecl(newSeed, IntegerType, FuncCall(pow, [seed, IntegerLit(2)])), VarDecl(s, StringType, FuncCall(to_string, [newSeed])), CallStmt(erase, s, BinExpr(-, BinExpr(+, FuncCall(begin, []), FuncCall(size, [s])), IntegerLit(2)), FuncCall(end, [s])), ReturnStmt(FuncCall(stoi, [FuncCall(substr, [s, BinExpr(-, FuncCall(size, [s]), IntegerLit(4))])]))]))
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
	FuncDecl(digitExtraction, IntegerType, [Param(seed, IntegerType), Param(extractDigits, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([VarDecl(s, StringType, StringLit()), VarDecl(strSeed, StringType, FuncCall(to_string, [seed])), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, size), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(s, BinExpr(+, s, ArrayCell(strSeed, [ArrayCell(extractDigits, [i])])))])), ReturnStmt(FuncCall(stoi, [s]))]))
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
	FuncDecl(foldShift, IntegerType, [Param(key, IntegerType), Param(addressSize, IntegerType)], None, BlockStmt([VarDecl(x, StringType, FuncCall(to_string, [key])), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, FuncCall(length, [x])), BinExpr(+, i, IntegerLit(1)), BlockStmt([VarDecl(s, StringType, FuncCall(substr, [x, i, addressSize])), AssignStmt(i, BinExpr(+, i, addressSize)), AssignStmt(sum, BinExpr(+, sum, FuncCall(stoi, [s])))])), VarDecl(test, IntegerType, FuncCall(pow, [IntegerLit(10), addressSize])), ReturnStmt(BinExpr(%, sum, test))]))
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
	FuncDecl(rotation, IntegerType, [Param(key, IntegerType), Param(addressSize, IntegerType)], None, BlockStmt([VarDecl(x, StringType, FuncCall(to_string, [key])), VarDecl(temp, StringType, ArrayCell(x, [BinExpr(-, FuncCall(length, [x]), IntegerLit(1))])), ForStmt(AssignStmt(i, BinExpr(-, FuncCall(length, [x]), IntegerLit(1))), BinExpr(>, i, IntegerLit(0)), BinExpr(-, i, IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(x, [i]), ArrayCell(x, [BinExpr(-, i, IntegerLit(1))]))])), AssignStmt(ArrayCell(x, [IntegerLit(0)]), temp), ReturnStmt(FuncCall(foldShift, [FuncCall(stoll, [x]), addressSize]))]))
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
	FuncDecl(minStr, StringType, [Param(S1, StringType), Param(S2, StringType), Param(sizeS1, IntegerType), Param(sizeS2, IntegerType)], None, BlockStmt([VarDecl(result, StringType, StringLit()), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<=, i, BinExpr(-, sizeS2, sizeS1)), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(result, BinExpr(::, S1, S2)), IfStmt(FuncCall(containStr, [S1, result]), BlockStmt([ReturnStmt(result)]))])), ReturnStmt(StringLit(Not found))]))
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
	FuncDecl(minStr, StringType, [Param(S1, StringType), Param(S2, StringType), Param(sizeS1, IntegerType), Param(sizeS2, IntegerType)], None, BlockStmt([VarDecl(result, StringType, StringLit()), ReturnStmt(StringLit(Not found))]))
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
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, nE), BinExpr(+, i, IntegerLit(1)), IfStmt(BinExpr(==, nE, BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(nE), AssignStmt(i, BinExpr(+, i, IntegerLit(1)))))]))
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
	FuncDecl(checkzero, BooleanType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(100)), VarDecl(nums, ArrayType([100], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(checkzero, nums, nE)]))
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
	FuncDecl(checkzero, BooleanType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([]))
	FuncDecl(recursive, VoidType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType), Param(index, IntegerType), Param(count, IntegerType), Param(sum, IntegerType), Param(minjump, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(100)), VarDecl(nums, ArrayType([100], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(recursive, nums, IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(1))]))
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
	FuncDecl(jump, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(100)), VarDecl(nums, ArrayType([100], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(jump, nums, IntegerLit(100))]))
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
	FuncDecl(reverseStr, StringType, [Param(str, StringType), Param(size, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, StringType, StringLit(Hello World!)), CallStmt(reverseStr, s, IntegerLit(12))]))
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
	FuncDecl(lengthOfLastWord, IntegerType, [Param(s, ArrayType([100], StringType)), Param(size, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, ArrayType([100], StringType), ArrayLit([StringLit(Hello World!), StringLit(s1), StringLit(s2)])), CallStmt(lengthOfLastWord, s, IntegerLit(100))]))
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
	FuncDecl(containStr, BooleanType, [Param(S1, StringType), Param(S2, StringType), Param(sizeS1, IntegerType), Param(sizeS2, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(S1, StringType, StringLit(OKOK)), VarDecl(S2, StringType, StringLit(okok)), CallStmt(lengthOfLastWord, S1, S2, IntegerLit(4), IntegerLit(4))]))
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
	FuncDecl(search, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(size, IntegerType), Param(target, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(100)), VarDecl(target, IntegerType, IntegerLit(20)), VarDecl(nums, ArrayType([100], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(search, nums, nE, target)]))
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
	FuncDecl(completeNum, BooleanType, [Param(N, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(completeNum, IntegerLit(10))]))
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
	FuncDecl(max_two_nums, AutoType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(max_two_nums, [IntegerLit(10), IntegerLit(20)]))]))
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
	FuncDecl(min_two_nums, AutoType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(min_two_nums, [IntegerLit(10), IntegerLit(20)]))]))
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
	FuncDecl(factorial, AutoType, [Param(N, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printFac, FuncCall(factorial, [IntegerLit(20)]))]))
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
	FuncDecl(findMax, AutoType, [Param(vals, ArrayType([100], IntegerType)), Param(numEls, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(100)), VarDecl(nums, ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(printMax, FuncCall(findMax, [nums, nE]))]))
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
	FuncDecl(findMax, AutoType, [Param(vals, ArrayType([100], IntegerType)), Param(numEls, IntegerType)], None, BlockStmt([]))
	FuncDecl(findMin, AutoType, [Param(vals, ArrayType([100], IntegerType)), Param(numEls, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(100)), VarDecl(nums, ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(print, FuncCall(findMax, [nums, nE])), CallStmt(print, FuncCall(findMin, [nums, nE]))]))
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
	FuncDecl(findMax, AutoType, [Param(vals, ArrayType([100], IntegerType)), Param(numEls, IntegerType)], None, BlockStmt([VarDecl(max, IntegerType, ArrayCell(vals, [IntegerLit(0)])), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, numEls), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(vals, [i]), max), BlockStmt([AssignStmt(max, ArrayCell(vals, [i]))]))])), ReturnStmt(max)]))
	FuncDecl(findMin, AutoType, [Param(vals, ArrayType([100], IntegerType)), Param(numEls, IntegerType)], None, BlockStmt([VarDecl(min, IntegerType, ArrayCell(vals, [IntegerLit(0)])), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, numEls), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(vals, [i]), min), BlockStmt([AssignStmt(min, ArrayCell(vals, [i]))]))])), ReturnStmt(min)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nE, IntegerType, IntegerLit(100)), VarDecl(nums, ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(print, FuncCall(findMax, [nums, nE])), CallStmt(print, FuncCall(findMin, [nums, nE]))]))
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
	FuncDecl(isPalindrome, BooleanType, [Param(str, ArrayType([100], StringType)), Param(strSize, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(str, ArrayType([100], StringType), ArrayLit([StringLit(), StringLit(2), StringLit(23423), StringLit(23432)])), VarDecl(nE, IntegerType, IntegerLit(100)), CallStmt(isPalindrome, str, nE)]))
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
            if (checkElementsUniqueness(nums, nE) == false) {
                print("element is unique");
            } else {
                print("element is not unique");
            }
        }
    """
        expect = """Program([
	FuncDecl(checkElementsUniqueness, BooleanType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nums, ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), VarDecl(nE, IntegerType, IntegerLit(100)), IfStmt(BinExpr(==, FuncCall(checkElementsUniqueness, [nums, nE]), BooleanLit(False)), BlockStmt([CallStmt(print, StringLit(element is unique))]), BlockStmt([CallStmt(print, StringLit(element is not unique))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90(self):
        input = """
        checkDuplicate: function boolean(ar: array[100] of integer, size: integer) {}
        main : function void () {
            nums: array[100] of integer = {100, 2, 3, 4};
            nE: integer = 100;
            if (checkDuplicate(nums, nE) == false) {
                print("");
            } else {
                print("");
            }
        }
    """
        expect = """Program([
	FuncDecl(checkDuplicate, BooleanType, [Param(ar, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nums, ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), VarDecl(nE, IntegerType, IntegerLit(100)), IfStmt(BinExpr(==, FuncCall(checkDuplicate, [nums, nE]), BooleanLit(False)), BlockStmt([CallStmt(print, StringLit())]), BlockStmt([CallStmt(print, StringLit())]))]))
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
	FuncDecl(gcdIteration, IntegerType, [Param(p, IntegerType), Param(q, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(p, IntegerType, IntegerLit(100)), VarDecl(q, IntegerType, IntegerLit(200)), CallStmt(print, FuncCall(gcdIteration, [p, q]))]))
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
	FuncDecl(gcdRecursion, IntegerType, [Param(p, IntegerType), Param(q, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, q, IntegerLit(0)), ReturnStmt(p)), ReturnStmt(FuncCall(gcdRecursion, [q, BinExpr(%, p, q)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(p, IntegerType, IntegerLit(100)), VarDecl(q, IntegerType, IntegerLit(200)), CallStmt(print, FuncCall(gcdRecursion, [p, q]))]))
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
	FuncDecl(recursiveSearch, IntegerType, [OutParam(n, IntegerType), Param(m, IntegerType), Param(arr, ArrayType([100], IntegerType)), Param(index, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(0)), VarDecl(m, IntegerType, IntegerLit(0)), VarDecl(index, IntegerType, IntegerLit(0)), VarDecl(arr, ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), CallStmt(print, FuncCall(recursiveSearch, [n, m, arr, index]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94(self):
        input = """
        isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {}
        main : function void () {
            size: integer = 100;
            head, tail: array[100] of integer = {100, 2, 3, 4}, {};
            if (isSymmetry(head, tail, size) == false) {
                print("array is symmetric");
            } else {
                print("array is not symmetric");
            }
        }
    """
        expect = """Program([
	FuncDecl(isSymmetry, BooleanType, [Param(head, ArrayType([100], IntegerType)), Param(tail, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(size, IntegerType, IntegerLit(100)), VarDecl(head, ArrayType([100], IntegerType), ArrayLit([IntegerLit(100), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), VarDecl(tail, ArrayType([100], IntegerType), ArrayLit([])), IfStmt(BinExpr(==, FuncCall(isSymmetry, [head, tail, size]), BooleanLit(False)), BlockStmt([CallStmt(print, StringLit(array is symmetric))]), BlockStmt([CallStmt(print, StringLit(array is not symmetric))]))]))
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
	FuncDecl(PARENT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([]))
	FuncDecl(LEFT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([]))
	FuncDecl(RIGHT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([]))
	FuncDecl(reheapUp, VoidType, [Param(maxHeap, ArrayType([100], IntegerType)), Param(numberOfElements, IntegerType), Param(index, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(index, IntegerType, IntegerLit(1)), VarDecl(maxHeap, ArrayType([100], IntegerType), ArrayLit([IntegerLit(1001), IntegerLit(20), IntegerLit(30), IntegerLit(40)])), CallStmt(reheapUp, maxHeap, IntegerLit(100), index)]))
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
	FuncDecl(PARENT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([]))
	FuncDecl(LEFT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([]))
	FuncDecl(RIGHT, IntegerType, [Param(i, IntegerType)], None, BlockStmt([]))
	FuncDecl(reheapDown, VoidType, [Param(maxHeap, ArrayType([100], IntegerType)), Param(numberOfElements, IntegerType), Param(index, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(index, IntegerType, IntegerLit(1)), VarDecl(maxHeap, ArrayType([100], IntegerType), ArrayLit([IntegerLit(1001), IntegerLit(20), IntegerLit(30), IntegerLit(40)])), CallStmt(reheapDown, maxHeap, IntegerLit(100), index)]))
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
	FuncDecl(buildMaxHeap, VoidType, [Param(arr, ArrayType([100], IntegerType)), Param(numOfEl, IntegerType)], None, BlockStmt([]))
	FuncDecl(heapSort, VoidType, [Param(start, ArrayType([100], IntegerType)), Param(numOfEl, IntegerType)], None, BlockStmt([CallStmt(buildMaxHeap, start, numOfEl)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(index, IntegerType, IntegerLit(1)), VarDecl(maxHeap, ArrayType([100], IntegerType), ArrayLit([IntegerLit(1001), IntegerLit(20), IntegerLit(30), IntegerLit(40)])), CallStmt(heapSort, maxHeap, IntegerLit(100)), CallStmt(print, maxHeap)]))
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
	FuncDecl(buildMaxHeap, VoidType, [Param(arr, ArrayType([100], IntegerType)), Param(numOfEl, IntegerType)], None, BlockStmt([]))
	FuncDecl(heapify, VoidType, [Param(arr, ArrayType([100], IntegerType)), Param(numOfEl, IntegerType), Param(i, IntegerType)], None, BlockStmt([]))
	FuncDecl(heapSort, VoidType, [Param(start, ArrayType([100], IntegerType)), Param(numOfEl, IntegerType)], None, BlockStmt([CallStmt(buildMaxHeap, start, numOfEl), CallStmt(buildMaxHeap, start, numOfEl), ForStmt(AssignStmt(i, BinExpr(-, numOfEl, IntegerLit(1))), BinExpr(>=, i, IntegerLit(0)), BinExpr(-, i, IntegerLit(1)), BlockStmt([VarDecl(temp, IntegerType, ArrayCell(start, [IntegerLit(0)])), AssignStmt(ArrayCell(start, [IntegerLit(0)]), ArrayCell(start, [i])), AssignStmt(ArrayCell(start, [i]), temp), CallStmt(heapify, start, i, IntegerLit(0))])), CallStmt(printArray, start, end)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(index, IntegerType, IntegerLit(1)), VarDecl(maxHeap, ArrayType([100], IntegerType), ArrayLit([IntegerLit(1001), IntegerLit(20), IntegerLit(30), IntegerLit(40)])), CallStmt(heapSort, maxHeap, IntegerLit(100))]))
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
	FuncDecl(swap, VoidType, [OutParam(x, IntegerType), OutParam(y, IntegerType)], None, BlockStmt([VarDecl(k, IntegerType, x), AssignStmt(x, y), AssignStmt(y, k)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(y, IntegerType, IntegerLit(3)), CallStmt(swap, x, y), CallStmt(print, BinExpr(+, BinExpr(+, x, y), StringLit()))]))
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
	FuncDecl(rotation, IntegerType, [Param(key, IntegerType), Param(addressSize, IntegerType)], None, BlockStmt([]))
	FuncDecl(midSquare, IntegerType, [Param(seed, IntegerType)], None, BlockStmt([]))
	FuncDecl(digitExtraction, IntegerType, [Param(seed, IntegerType), Param(extractDigits, ArrayType([100], IntegerType)), Param(size, IntegerType)], None, BlockStmt([]))
	FuncDecl(foldShift, IntegerType, [Param(key, IntegerType), Param(addressSize, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(midSquare, [IntegerLit(62323)])), CallStmt(print, FuncCall(foldShift, [IntegerLit(62323), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
