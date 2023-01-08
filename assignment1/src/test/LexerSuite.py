import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # Test Comment
    def test_1(self):
        input = "/* hello world \t\b\n Hello World*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test_2(self):
        input = """// hello world"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_3(self):
        input = "// hello world\n\t/*Hello world*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_4(self):
        input = "// x/*x*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))

    def test_5(self):
        input = "/* \n\t//x */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_6(self):
        input = "/* \n\t/*x*/ */"
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))

    # Test Identifiers
    def test_7(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))

    def test_8(self):
        input = "abc a12"
        expect = "abc,a12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 108))

    def test_9(self):
        input = "xyz A12"
        expect = "xyz,A12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))

    def test_10(self):
        input = "abc?svn"
        expect = "abc,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 110))

    def test_11(self):
        input = "0a12"
        expect = "0,a12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))

    def test_12(self):
        input = "_0a12"
        expect = "_0a12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))

    # Test Int Literals
    def test_13(self):
        input = "0 12 321 20342324"
        expect = "0,12,321,20342324,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))

    def test_14(self):
        input = "0 12_321 20_342_324"
        expect = "0,12321,20342324,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 114))

    def test_15(self):
        input = "1_234_567_"
        expect = "1234567,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))

    def test_16(self):
        input = "-323"
        expect = "-,323,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))

    # Test Float Literals
    def test_17(self):
        input = "0.0"
        expect = "0.0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test_18(self):
        input = "1.001"
        expect = "1.001,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))

    def test_19(self):
        input = "0.200000"
        expect = "0.200000,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))

    def test_20(self):
        input = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 120))

    def test_21(self):
        input = "1_234."
        expect = "1234.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 121))

    def test_22(self):
        input = "11e8 0.37E-3 123e+41 1_2_8e-42"
        expect = "11e8,0.37E-3,123e+41,128e-42,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 122))
