import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # ParserQuiz1
    # def test_1(self):
    #     input = """vardecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 101))
    #
    # def test_2(self):
    #     input = """funcdecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 102))
    #
    # def test_3(self):
    #     input = """vardecl funcdecl vardecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 103))
    #
    # def test_4(self):
    #     input = """vardecl vardecl vardecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 104))
    #
    # def test_5(self):
    #     input = """funcdecl funcdecl funcdecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 105))
    #
    # def test_6(self):
    #     input = """funcdecl
    #             vardecl
    #             vardecl
    #             funcdecl
    #             funcdecl
    #             vardecl
    #             funcdecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 106))
    #
    # def test_7(self):
    #     input = """"""
    #     expect = "Error on line 1 col 0: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 107))

    # ParserQuiz2
    #     def test_8(self):
    #         input = """int a, b,c;
    #                 float foo(int a; float c, d) body
    #                 float goo (float a, b) body"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 201))
    #
    #     def test_9(self):
    #         input = """int a, b,;"""
    #         expect = "Error on line 1 col 9: ;"
    #         self.assertTrue(TestParser.test(input, expect, 202))
    #
    #     def test_10(self):
    #         input = """float foo(int a, float c, d) body"""
    #         expect = "Error on line 1 col 17: float"
    #         self.assertTrue(TestParser.test(input, expect, 203))
    #
    #     def test_11(self):
    #         input = """float foo(int a; float c, d;) body"""
    #         expect = "Error on line 1 col 28: )"
    #         self.assertTrue(TestParser.test(input, expect, 204))
    #
    #     def test_12(self):
    #         input = """int c;
    # float A()"""
    #         expect = "Error on line 2 col 9: <EOF>"
    #         self.assertTrue(TestParser.test(input, expect, 205))
    #
    #     def test_13(self):
    #         input = """int c
    # float A() body"""
    #         expect = "Error on line 2 col 0: float"
    #         self.assertTrue(TestParser.test(input, expect, 206))
    #
    #     def test_14(self):
    #         input = """int a, b,c;
    # float foo(int a; float c, d) body
    # int c,d;
    # float goo (float a, b) body
    # int"""
    #         expect = "Error on line 5 col 3: <EOF>"
    #         self.assertTrue(TestParser.test(input, expect, 207))
    #
    #     def test_15(self):
    #         input = """float foo() body
    #                 int foo() body
    #                 float foo(int a) body"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 208))
    #
    #     def test_16(self):
    #         input = """int a;
    #                 float b,c;
    #                 int a;"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 209))
    #
    #     def test_17(self):
    #         input = "int a,b,c;"
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 210))

    # ParserQuiz3
    #     def test_18(self):
    #         input = """int a, b,c;
    # float foo(int a; float c, d) {
    #    int e ;
    #    e = expr ;
    #    c = expr ;
    #    foo(expr);
    #    return expr;
    # }
    # float goo (float a, b) {
    #    return expr;
    # }"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 301))
    #
    #     def test_19(self):
    #         input = """int a, b,;"""
    #         expect = "Error on line 1 col 9: ;"
    #         self.assertTrue(TestParser.test(input, expect, 302))
    #
    #     def test_20(self):
    #         input = """int a, b,;"""
    #         expect = "Error on line 1 col 9: ;"
    #         self.assertTrue(TestParser.test(input, expect, 303))
    #
    #     def test_21(self):
    #         input = """float foo(int a, float c, d) {}"""
    #         expect = "Error on line 1 col 17: float"
    #         self.assertTrue(TestParser.test(input, expect, 304))
    #
    #     def test_22(self):
    #         input = """float foo(int a; float c, d;) {}"""
    #         expect = "Error on line 1 col 28: )"
    #         self.assertTrue(TestParser.test(input, expect, 305))
    #
    #     def test_23(self):
    #         input = """int c;
    # c = expr;"""
    #         expect = "Error on line 2 col 0: c"
    #         self.assertTrue(TestParser.test(input, expect, 306))
    #
    #     def test_24(self):
    #         input = """
    # c = expr;"""
    #         expect = "Error on line 2 col 0: c"
    #         self.assertTrue(TestParser.test(input, expect, 307))
    #
    #     def test_25(self):
    #         input = """int a, b,c;
    # float foo(int a; float c, d) {
    #    int e = expr;
    #    e = expr ;
    #    c = expr ;
    #    return expr;
    # }
    # float goo(float a, b) {
    #    return expr;
    # }"""
    #         expect = "Error on line 3 col 9: ="
    #         self.assertTrue(TestParser.test(input, expect, 308))
    #
    #     def test_26(self):
    #         input = """int a, b,c;
    # float foo(int a; float c, d) {
    #    int e ;
    #    e = expr ;
    #    c = expr ;
    #    return expr
    # }
    # """
    #         expect = "Error on line 7 col 0: }"
    #         self.assertTrue(TestParser.test(input, expect, 309))
    #
    #     def test_27(self):
    #         input = """float goo (float a, b) {
    #     foo(expr, expr, expr);
    #     return expr;
    # }
    #
    # c = expr;"""
    #         expect = "Error on line 6 col 0: c"
    #         self.assertTrue(TestParser.test(input, expect, 310))
    #
    #     def test_28(self):
    #         input = """float goo (float a, b) {
    #    return expr;
    # }"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 311))

    # ParserQuiz4
    def test_29(self):
        input = """int a, b,c;
    float foo(int a; float c, d) {
       int e ;
       e = a + 4 ;
       c = a * d / 2.0 ;
       return c + 1;
    }
    float goo (float a, b) {
       return foo(1, a, b);
    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 401))

    def test_30(self):
        input = """int a, b,;"""
        expect = "Error on line 1 col 9: ;"
        self.assertTrue(TestParser.test(input, expect, 402))

    def test_31(self):
        input = """float foo(int a, float c, d) {}"""
        expect = "Error on line 1 col 17: float"
        self.assertTrue(TestParser.test(input, expect, 403))

    def test_32(self):
        input = """float foo(int a; float c, d;) {}"""
        expect = "Error on line 1 col 28: )"
        self.assertTrue(TestParser.test(input, expect, 404))

    def test_33(self):
        input = """int c;
    c = 4;"""
        expect = "Error on line 2 col 4: c"
        self.assertTrue(TestParser.test(input, expect, 405))

    def test_34(self):
        input = """int a, b,c;
    float foo(int a; float c, d) {
       int e = 5;
       e = a + 4 ;
       c = a * d / 2.0 ;
       return c + 1;
    }
    float goo(float a, b) {
       return foo(1, a, b);
    }"""
        expect = "Error on line 3 col 13: ="
        self.assertTrue(TestParser.test(input, expect, 406))

    def test_35(self):
        input = """int a, b,c;
    float foo(int a; float c, d) {
       int e ;
       e = a + 4 ;
       c = a * d / 2.0 ;
       return c + 1
    }
    float goo (float a, b) {
       return foo(1, a, b);
    }"""
        expect = "Error on line 7 col 4: }"
        self.assertTrue(TestParser.test(input, expect, 407))

    def test_36(self):
        input = """float goo (float a, b) {
       return foo(1, a, b);
    }

    c = 5;"""
        expect = "Error on line 5 col 4: c"
        self.assertTrue(TestParser.test(input, expect, 408))

    def test_37(self):
        input = """float goo (float a, b) {
       return foo(1, a, b) + 1;
    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 409))

    def test_38(self):
        input = """float goo (float a, b) {
       return 1 - foo(1, a, b);
    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 410))

    def test_39(self):
        input = """int a, b,c;
    float foo(int a; float c, d) {
       int e ;
       e = a + 4 ;
       c = a * d / 2.0 ;
       return c + 1;
    }
    float goo (float a, b) {
       return foo(1, a, b);
    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 411))
