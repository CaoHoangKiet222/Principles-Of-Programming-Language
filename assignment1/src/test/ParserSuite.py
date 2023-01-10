import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # Test Variable Declarations
    #     def test_1(self):
    #         input = """
    # a, b, c : boolean;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 200))
    #
    #     def test_2(self):
    #         input = """
    # a,b,c,d: string;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 201))
    #
    #     def test_3(self):
    #         input = """
    # a,   b,   c   : auto = expr , expr , expr;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 202))
    #
    #     def test_4(self):
    #         input = """
    # a,   b,   c   : auto = expr , expr;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 203))
    #
    #     def test_5(self):
    #         input = """
    # a,   b,   c   : auto;
    # """
    #         expect = "Error on line 2 col 20: ;"
    #         self.assertTrue(TestParser.test(input, expect, 204))
    #
    #     def test_6(self):
    #         input = """
    # a,   b,   c   : array [2, 3] of int;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 205))
    #
    #     def test_7(self):
    #         input = """
    # a, b, c : int = expr;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 206))
    #
    #     def test_8(self):
    #         input = """
    # a,   b,   c   : array [2, 3] of int;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 207))
    #
    #     def test_9(self):
    #         input = """
    # a,   b,   c   : array [2, 3] of int = expr, expr;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 208))
    #
    #     def test_10(self):
    #         input = """
    # a,   b,   c   : array [2, 3] of int = expr, expr, expr;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 209))

    def test_11(self):
        input = """
        x : int = 65;
        fact : function int (n : int) {
            if (n == 0) return 1;
            else return n*fact(n-1);
        }
        main : function void () {
            delta : int = fact(3);
            inc (x, delta);
            printint(x);
        }
        inc : function void (out n: int, delta : int) {
            n = n + delta;
        }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

#     def test_12(self):
#         input = """
#         (c + e + d) >= 2,
#         (c >= 2) == true,
#         true && true,
#         b[a[2, 3],c[2, 5]] + d,
#         a::b::c,
#         1 > 2 && (2 > 3),
#         -a,
#         !!true
# """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 211))

    # # # Test Array Literals # # #
    def test_38(self):
        input = "{1, 5, 7, 12}"
        expect = "{1, 5, 7, 12},<EOF>"
        self.assertTrue(TestParser.test(input, expect, 138))

    def test_39(self):
        input = "{\"Kangxi\", \"Yongzheng\", \"Qianlong\"}"
        expect = "{\"Kangxi\", \"Yongzheng\", \"Qianlong\"},<EOF>"
        self.assertTrue(TestParser.test(input, expect, 139))

    def test_40(self):
        input = "{1 + 2, 3 + 4, 5 + 6}"
        expect = "{1 + 2, 3 + 4, 5 + 6},<EOF>"
        self.assertTrue(TestParser.test(input, expect, 140))

    def test_41(self):
        input = "{a[1+2, 3], b[1+3, 4]}"
        expect = "{a[1+2, 3], b[1+3, 4]},<EOF>"
        self.assertTrue(TestParser.test(input, expect, 141))
