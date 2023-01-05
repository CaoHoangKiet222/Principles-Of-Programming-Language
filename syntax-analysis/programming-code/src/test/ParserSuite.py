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
    def test_8(self):
        input = """int a, b,c;
                float foo(int a; float c, d) body
                float goo (float a, b) body"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_9(self):
        input = """int a, b,;"""
        expect = "Error on line 1 col 9: ;"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_10(self):
        input = """float foo(int a, float c, d) body"""
        expect = "Error on line 1 col 17: float"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_11(self):
        input = """float foo(int a; float c, d;) body"""
        expect = "Error on line 1 col 28: )"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_12(self):
        input = """int c;
float A()"""
        expect = "Error on line 2 col 9: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_13(self):
        input = """int c
float A() body"""
        expect = "Error on line 2 col 0: float"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_14(self):
        input = """int a, b,c;
float foo(int a; float c, d) body
int c,d;
float goo (float a, b) body
int"""
        expect = "Error on line 5 col 3: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_15(self):
        input = """float foo() body
                int foo() body
                float foo(int a) body"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_16(self):
        input = """int a;
                float b,c;
                int a;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_17(self):
        input = "int a,b,c;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
