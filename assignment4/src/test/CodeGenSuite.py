import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_1(self):
    #     input = """
    #     main: function void() {
    #         printInteger(10);
    #     }
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))

    # def test_2(self):
    #     input = """
    #     main: function void() {
    #         x: integer = 10;
    #         printInteger(x);
    #     }
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))

    # def test_3(self):
    #     input = """
    #     x, y: integer = 1, 2;
    #     main: function void() {
    #         x: integer = 10;
    #         printInteger(x);
    #     }
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))

    # def test_4(self):
    #     input = """
    #     x: integer = 1;
    #     main: function void() {
    #         printInteger(x);
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_5(self):
        input = """
        x: integer = 1;
        main: function void() {
            // printInteger(x);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 505))
