import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # # # Test Variable Declarations # # #
    def test_1(self):
        input = """
    a, b, c : boolean;
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        input = """
    a,b,c,d: string;
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_3(self):
        input = """
    a,   b,   c   : auto = 1 , 2 , 3;
    a,   b,   c   : auto = 1 , 2;
    """
        expect = "Error on line 3 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_4(self):
        input = """
    a,   b,   c   : auto = "hello_a" , "hello_b", "hello_c" ;
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_5(self):
        input = """
    a,   b,   c   : float = 2.000001, 3.0000001, 40_1.1;
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_6(self):
        input = """
    a,   b,   c   : boolean = true, false, true;
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_7(self):
        input = """
    a, b, c : integer = 20_342_324, -2000, 1_234;
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_8(self):
        input = """
    a,   b,   c   : array [2, 3] of integer;
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_9(self):
        input = """
    a,   b,   c   : array [2, 3] of integer = {{1, 2, 3}, {0, 5, 6}}, {{}, {}}, {{2, 3}, {}};
    a2, b2, c2   : array [2, 3] of float = {{1.33333, .5555e-2, 189.00000}, {157., 1_2_3_4., 1_2_3_56.1234}}, {{}, {}}, {{1.34, 12e8}, {}};
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_10(self):
        input = """
    a,   b,   c   : array [2] of integer = {1, 2}, {}, {3000, 2000};
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_11(self):
        input = """
    a, b, c : array [2] of string = {"x", "y"}, {"z"}, {};
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_12(self):
        input = """
    a, b, c : array [2] of boolean = {false, true}, {true}, {false};
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_13(self):
        input = """
    a, b, c : array [2] of = {false, true}, {true}, {false};
    """
        expect = "Error on line 2 col 27: ="
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_14(self):
        input = """
    a, b, c boolean;
    """
        expect = "Error on line 2 col 12: boolean"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_15(self):
        input = """
        a, b, c : integer = -1, 0, 3;
        y, z : integer = 1, 1;
        x : array [0, 100] of integer;
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    # # # Test Function Declarations # # #
    def test_16(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_17(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_18(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_19(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_20(self):
        input = """
        main: function void() {
            for (i = 1, i < 100, i+1) {
                j : integer = 0;
                while (j < 200) {j = j+1;}
                while (i != 20) {}
            }
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_21(self):
        input = """
        main: function void() {
            for (i = 1 i < 100 i+1) {
                j : integer = 0;
                while (j < 200) {j = j+1;}
                while (i != 20) {}
            }
        }
    """
        expect = "Error on line 3 col 23: i"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_22(self):
        input = """
        main: function void() {
            x : integer = 1;
            for (i = 1, i < 100, i+1) {
                foo(x + 1, foo(i + 1, foo(x + 2, 1)));
            }
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_23(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_24(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_25(self):
        input = """
        Checkzero: function boolean(nums: array[100] of integer, size: integer) {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_26(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

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
        main : function void () {
            reverse_string("Hello World!", 12);
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_28(self):
        input = """
        jump: function integer(nums: array[100] of integer, size: integer) {
          minjump: integer = size - 1;
          Recursive(nums, 0, 0, 0, minjump);
          return minjump;
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_29(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_31(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_32(self):
        input = """
      lengthOfLastWord: function integer(s: array[100] of string, size: integer) {
        count: integer = 0;
        if (size == 0)
          return 0
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
        expect = "Error on line 6 col 8: i"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_33(self):
        input = """
      lengthOfLastWord: function integer(s: array[100] of string, size: integer) {
        count: integer = 0;
        if (size == 0)
          return 0;

        i: integer = size - 1,
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
        expect = "Error on line 8 col 8: while"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_34(self):
        input = """
      helloWorld: function integer() {return -1;}
      lengthOfLastWord: function integer() inherit helloWorld {
        return 0;
      }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_35(self):
        input = """
      lengthOfLastWord: function integer() inherit {
        return 0;
      }
    """
        expect = "Error on line 2 col 51: {"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_36(self):
        input = """
      lengthOfFirstWord: function auto() {return "";}
      lengthOfLastWord: function auto() inherit lengthOfFirstWord {
        return "lengthOfLastWord";
      }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_37(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_38(self):
        input = """
        max_two_nums: function auto (a: integer, b: integer) {
            if (a > b) {
                return a;
            }
            return b;
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_39(self):
        input = """
        min_two_nums: function auto (a: integer, b: integer) {
            if (a < b) {
                return a;
            }
            return b;
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_40(self):
        input = """
        factorial: function auto(N: integer) {
          result: integer = 1;
          for (i = 1, i <= N, i+1) {
            result = result * i;
          }
          return result;
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_41(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_42(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_43(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_44(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_45(self):
        input = """
        checkElementsUniqueness: function boolean (arr: array[100] of integer, n: integer) {
          if ((n > 1000) || (n < 0))
            return false;
          for (i = 0, i < n - 1, i+1) {
            for (j = i + 1, j < n, j+1) {
              if (arr[i] == arr[j]))
                return false;
            }
          }
          return true;
        }
    """
        expect = "Error on line 7 col 35: )"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_46(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_47(self):
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
              less_size = less_size + 1
            } else {
              greater[greater_size] = ar[i];
              greater_size = greater_size + 1;
            }
          }

          return checkDuplicate(less, less_size) &&
                 checkDuplicate(greater, greater_size);
        }
    """
        expect = "Error on line 16 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_48(self):
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
        }
    """
        expect = "Error on line 23 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_49(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_50(self):
        input = """
        gcdRecursion: function integer(p: integer, q: integer) {
          if (q == 0)
            return p;
          return gcdRecursion(q, p % q);
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_51(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_52(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_53(self):
        input = """
        less_zero: boolean = false;
        c: integer = 0;

        printegerPattern: function void(n: integer) {
          if (n <= 0) {
            less_zero = true;
          }

          if (less_zero) {
            c = c - 1
            if (c == -1)
              return;
            printegerPattern(n + 5);
          } else {
            c = c + 1
            printegerPattern(n - 5);
          }
        }
    """
        expect = "Error on line 12 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_54(self):
        input = """
        isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (i = 0, i < size / 2, i+1) {
            if (head[i] != tail[i])
              return false;
          }
          return true;
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_55(self):
        input = """
        isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (i = 0, i < size / 2, i+1) {
            if (head[i] != tail[i])
              return false;
          }
          true;
        }
    """
        expect = "Error on line 7 col 10: true"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_56(self):
        input = """
        isSymmetry: function auto(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (i = 0, i < size / 2, i+1) {
            if (head[i] != tail[i])
              false;
          }
          true;
        }
    """
        expect = "Error on line 5 col 14: false"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_57(self):
        input = """
        isSymmetry: function auto(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (i = 0, i < size / 2, i+1) {
            if (head[i] != tail[i])
              false;
          }
          true;
        }
    """
        expect = "Error on line 5 col 14: false"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_58(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_59(self):
        input = """
        countWaysUtil: function integer(x: integer, num: integer) {
          val: integer = (x - num*num);
          if (val == 0)
            return 1;
          if (val < 0)
            return 0;

          return countWaysUtil(val, num + 1)  countWaysUtil(x, num + 1);
        }
    """
        expect = "Error on line 9 col 46: countWaysUtil"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60(self):
        input = """
        countWaysUtil: function integer(x: integer, num: integer) {
          val: integer = (x - num*num);
          if (val == 0)
            return 1;
          if (val < 0)
            return 0;

          return countWaysUtil(val, num + 1)  countWaysUtil(x, num + 1);
        }
    """
        expect = "Error on line 9 col 46: countWaysUtil"
        self.assertTrue(TestParser.test(input, expect, 260))

    # # # Test mix # # #
    def test_61(self):
        input = """
        a, b, c : integer = -1, 0, 3;
        y, z : integer = 1, 1;
        x : array [0, ] of integer;
        main: function void() {
            for (,,) {
                a = b + c;
                x[0, i] = y % z;
            }
        }
    """
        expect = "Error on line 4 col 22: ]"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_62(self):
        input = """
        x : array [0, 100] of integer;
        main: function void() {
            for (i = 1, i < 100, i+1) {
                if (i % 2 == 0) {
                    x[i, 0] = i;
                } ese {
                    x[0, i] = i + 1;
                }
            }
        }
    """
        expect = "Error on line 7 col 22: {"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_63(self):
        input = """
        main: function void() {
            for (i = 1, i < 100, i+1) {
                j : integer = 0;
                while () {
                    if (i + j >= 20) {
                        break;
                    } else {
                     j = j + 1;
                    }
                }
            }
        }
    """
        expect = "Error on line 5 col 23: )"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64(self):
        input = """
        main: function void() {
            for (i = 1, i < 100, i+1) {
                j : integer = 0;
                while (j) {
                    if () {
                        break;
                    } else {
                     j = j + 1;
                    }
                }
            }
        }
    """
        expect = "Error on line 6 col 24: )"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_65(self):
        input = """
        main: function void() {
            for (i = 1, i < 100, i+1) {
                j : integer = 0;
                while (j) {
                    if (i + j >= 20) {
                        ;
                    } else {
                     ;
                    }
                }
            }
        }
    """
        expect = "Error on line 7 col 24: ;"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_66(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT: function integer(i: integer) { return (2 * i + 1); }

        RIGHT: function integer(i: integer) { return (2 * i + 2); }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_67(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_68(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT: integer(i: integer) { return (2 * i + 1); }

        RIGHT: integer(i: integer) { return (2 * i + 2); }

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
        expect = "Error on line 4 col 21: ("
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_69(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT:  function integer(i: integer) { return (2 * i + 1); }

        RIGHT: function integer(i: integer) { return (2 * i + 2); }

        reheapUp: function void (maxHeap: array [] of integer, numberOfElements: integer, index: integer)
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
        expect = "Error on line 8 col 49: ]"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_70(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT:  function integer(i: integer) { return (2 * i + 1); }

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
    """
        expect = "Error on line 20 col 4: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT:  function integer(i: integer) { return (2 * i + 1); }

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_72(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT:  function integer(i: integer) { return (2 * i + 1); }

        RIGHT: function integer(i: integer) { return (2 * i + 2); }

        reheapDown: function void(maxHeap: array [100] of integer, numberOfElements: integer, index: integer)
        {
            if (index >= numberOfElements) {
                return;
            }
            left: integer = LEFT(index);
            right: integer = RIGHT(index);

            largest: integer = index;

            if (left <  && (maxHeap[left] > maxHeap[index])) {
                largest = left;
            }

            if (right <  && (maxHeap[right] > maxHeap[largest])) {
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
        expect = "Error on line 18 col 24: &&"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_73(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT:  function integer(i: integer) { return (2 * i + 1); }

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
                temp:  = maxHeap[index];
                maxHeap[index] = maxHeap[largest];
                maxHeap[largest] = temp;
                reheapDown(maxHeap, numberOfElements, largest);
            }
        }
    """
        expect = "Error on line 28 col 23: ="
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74(self):
        input = """
        PARENT: function integer(i: integer) { return (i - 1) / 2; }

        LEFT:  function integer(i: integer) { return (2 * i + 1); }

        RIGHT: function integer(i: integer) { return (2 * i + 2); }

        reheapDown: void(maxHeap: array [100] of integer, numberOfElements: integer, index: integer)
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

            if (right < && (maxHeap[right] > maxHeap[largest])) {
                largest = right;
            }

            if (largest != index)
            {
                temp:  = maxHeap[index];
                maxHeap[] = maxHeap[largest];
                maxHeap[largest] = temp;
                reheapDown(maxHeap, numberOfElements, largest);
            }
        }
    """
        expect = "Error on line 8 col 20: void"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_75(self):
        input = """
      buildMaxHeap: function void(arr: array[100] of integer, numOfEl: integer) {
        for (i = numOfEl / 2 - 1, i >= 0, i-1) {
          heapify(arr, numOfEl, i);
        }
      }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_76(self):
        input = """
      buildMaxHeap: function void(arr: array[100] of integer, integer numOfEl) {
        for (i = numOfEl / 2 - 1, i >= 0, i-1) {
          heapify(arr, numOfEl, i);
        }
      }
    """
        expect = "Error on line 2 col 62: integer"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_77(self):
        input = """
         moduloDivision: function integer(seed: integer, mod: integer) { return seed % mod; }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_78(self):
        input = """
         moduloDivision: function integer {seed: integer, mod: integer} { return seed % mod; }
    """
        expect = "Error on line 2 col 42: {"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_79(self):
        input = """
         moduloDivision: function integer (seed: integer, mod: integer) ( return seed % mod; )
    """
        expect = "Error on line 2 col 72: ("
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_80(self):
        input = """
         1moduloDivision: function integer (seed: integer, mod: integer) { return seed % mod; }
    """
        expect = "Error on line 2 col 9: 1"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_81(self):
        input = """
        main: function void() {
            for {i = 1, i < 100, i+1} {
                j : integer = 0;
                while (j < 200) {j = j+1;}
                while (i != 20) {}
            }
        }
    """
        expect = "Error on line 3 col 16: {"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_82(self):
        input = """
        Recursive: function void (nums: array[100] of integer, size: integer, index: integer , count: integer, sum: integer , minjump: integer) {
          if (sum >= size) {
            if (minjump > count)
              minjump = count;
          } else {
            for (i = 1, i <= nums[index], i + 1) {
              Recursive(nums, , count + 1, sum + i, );
            }
          }
        }
    """
        expect = "Error on line 8 col 30: ,"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_83(self):
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

        jump: function integer(nums: array[100] of integer, size: integer) {
          minjump: integer = size - 1;
          Recursive(nums, 0, 0, 0, minjump);
          return minjump;
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84(self):
        input = """
        Recursive: function void (nums: array[100] of integer, size: integer, index: integer , count: integer, sum: integer , minjump: integer) {
        };

        jump: function integer(nums: array[100] of integer, size: integer) {
        };
    """
        expect = "Error on line 3 col 9: ;"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_85(self):
        input = """
        Recursive: function void (nums: array[100] of integer; size: integer; index: integer ; count: integer; sum: integer , minjump: integer) {
        };

        jump: function integer(nums: array[100] of integer, size: integer) {
        };
    """
        expect = "Error on line 2 col 61: ;"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_86(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_87(self):
        input = """
        binarySearch: function integer(arr: array[1000] of integer, left: integer, right: integer, x: integer) {
          if {right >= left} {
            mid:integer = left + (right - left) / 2;
            if {arr[mid] == x}
              return mid;

            if (arr[mid] > x]
              return binarySearch(arr, left, mid - 1, x);

            return binarySearch(arr, mid + 1, right, x);
          }

          return -1;
        }
    """
        expect = "Error on line 3 col 13: {"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_88(self):
        input = """
        binarySearch: function integer(arr: array[1000] of integer, left: integer, right: integer, x: integer) {
          /* if {right >= left} {
            mid:integer = left + (right - left) / 2;
            if {arr[mid] == x}
              return mid;

            if (arr[mid] > x]
              return binarySearch(arr, left, mid - 1, x);

            return binarySearch(arr, mid + 1, right, x);
          } */

          return -1;
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input = """
        checkDuplicate: function boolean(ar: array[100] of integer, size: integer) {
          if (size <= 1)
            return true;

          // return checkDuplicate(less, less_size);
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90(self):
        input = """
        // checkDuplicate: function boolean(ar: array[100] of integer, size: integer) {
          if (size <= 1)
            return true;

          return checkDuplicate(less, less_size);
        }
    """
        expect = "Error on line 3 col 10: if"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92(self):
        input = """
        // /* checkDuplicate: function boolean(ar: array[100] of integer, size: integer) {
          if (size <= 1)
            return true;

          return checkDuplicate(less, less_size);
        */
    """
        expect = "Error on line 3 col 10: if"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_93(self):
        input = """
        checkElements: function boolean (arr: array[100] of integer, n: integer) {
          if ((n > 1000) || (n < 0))
            return false;
          for (i = 0, i < n - 1, i+1) {
            for (j = i + 1, j < n, j+1) {
              if (arr[i] == arr[j]/*)*/)
                return false;
            }
          }
          return true;
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94(self):
        input = """
        gcdRecursion: function integer(p: integer; q: integer) {
          if (q == 0)
            return p;
          return gcdRecursion(q, p % q);
        }
    """
        expect = "Error on line 2 col 49: ;"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_95(self):
        input = """
        gcdRecursion: auto function (p: integer, q: integer) {
          if (q == 0)
            return p;
          return gcdRecursion(q, p % q);
        }
    """
        expect = "Error on line 2 col 27: function"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_96(self):
        input = """
        isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (/*i = 0, i < size / 2, i+1*/) {
            if (head[i] != tail[i])
              return false;
          }
          return true;
        }
    """
        expect = "Error on line 3 col 43: )"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_97(self):
        input = """
        symmetry: function boolean(head: ar[100] of integer, tail: arr[100] of integer, size: integer) {
          for (i = 0, i < size / 2, i+1) {
            if (head[i] != tail[i])
              return false;
          }
          return true;
        }
    """
        expect = "Error on line 2 col 41: ar"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_98(self):
        input = """
        symmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (i = 0, /*i < size / 2*/, i+1) {
            if (head[i] != tail[i])
              return false;
          }
          return true;
        }
    """
        expect = "Error on line 3 col 38: ,"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99(self):
        input = """
        countWaysUtil: function integer(x: integer, num: integer) {
          val: integer = (x - num*num);
          if (val == 0)
            return 1;
          if (val < 0)
            return 0;

          return countWaysUtil(val, num + 1);  //countWaysUtil(x, num + 1)
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_100(self):
        input = """
        countWaysUtil: function integer(x: integer, num: integer) {
          val: integer = (x - num*);
          if (val == 0)
            return 1;
          if (val < 0)
            return 0;

          return countWaysUtil(val, num + 1);  //countWaysUtil(x, num + 1)
        }
    """
        expect = "Error on line 3 col 34: )"
        self.assertTrue(TestParser.test(input, expect, 300))
