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

    # def test_5(self):
    #     input = """
    #     x: integer = 1;
    #     main: function void() {
    #         printInteger(x);
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    # def test_6(self):
    #     input = """
    #     x: float = 1;
    #     main: function void() {
    #         writeFloat(x);
    #     }
    #     """
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test_7(self):
    #     input = """
    #     x: boolean = true;
    #     main: function void() {
    #         printBoolean(x);
    #     }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))

    # def test_8(self):
    #     input = """
    #     x: string = "111111";
    #     main: function void() {
    #         printString(x);
    #     }
    #     """
    #     expect = "111111"
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))

    # def test_9(self):
    #     input = """
    #     main: function void() {
    #         printInteger(10 + 1);
    #     }
    #     """
    #     expect = "11"
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))

    # def test_10(self):
    #     input = """
    #     main: function void() {
    #         writeFloat(10 + 1.1);
    #     }
    #     """
    #     expect = "11.1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))

    # def test_11(self):
    #     input = """
    #     main: function void() {
    #         writeFloat(100.1 + 1);
    #     }
    #     """
    #     expect = "101.1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))

    # def test_12(self):
    #     input = """
    #     main: function void() {
    #         writeFloat(100.1 + 20_1.2);
    #     }
    #     """
    #     expect = "301.3"
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))

    # def test_13(self):
    #     input = """
    #     main: function void() {
    #         printInteger(100 * 20);
    #     }
    #     """
    #     expect = "2000"
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))

    # def test_14(self):
    #     input = """
    #     main: function void() {
    #         printInteger(100 - 20);
    #         writeFloat(100.0 - 20);
    #         writeFloat(100 - 20.0);
    #         writeFloat(100.0 - 20.0);
    #     }
    #     """
    #     expect = "8080.080.080.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))

    # def test_15(self):
    #     input = """
    #     main: function void() {
    #         printInteger(1000 * 10);
    #         writeFloat(1000 * 20.25);
    #         writeFloat(1000.0 * 20);
    #         writeFloat(1000.0 * 20.25);
    #     }
    #     """
    #     expect = "1000020250.020000.020250.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))

    # def test_16(self):
    #     input = """
    #     main: function void() {
    #         writeFloat(100 / 20);
    #         writeFloat(100 / 20.0);
    #         writeFloat(100.0 / 20);
    #         writeFloat(100.0 / 20.0);
    #     }
    #     """
    #     expect = "5.05.05.05.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test_17(self):
    #     input = """
    #     main: function void() {
    #         printInteger(100 % 20);
    #     }
    #     """
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))

    # def test_18(self):
    #     input = """
    #     main: function void() {
    #       printString("hello"::"world");
    #     }
    #     """
    #     expect = "helloworld"
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test_19(self):
    #     input = """
    #     main: function void() {
    #         printString(("hello"::"world")::" with kiet");
    #     }
    #     """
    #     expect = "helloworld with kiet"
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))

    # def test_20(self):
    #     input = """
    #     main: function void() {
    #         printBoolean(true && false);
    #     }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test_21(self):
    #     input = """
    #     main: function void() {
    #         printBoolean(false || true && false || (false || true));
    #     }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # def test_22(self):
    #     input = """
    #     main: function void() {
    #         printBoolean((2 > 1) && 3 < 4);
    #         printBoolean((2.0 > 1) && 3 < 4);
    #     }
    #     """
    #     expect = "truetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))

    # def test_23(self):
    #     input = """
    #     main: function void() {
    #         printBoolean(!true);
    #         printBoolean(!(true && false));
    #     }
    #     """
    #     expect = "falsetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_24(self):
        input = """
        main: function void() {
            printInteger(-1);
            printInteger(-1 + 2);
        }
        """
        expect = "-11"
        self.assertTrue(TestCodeGen.test(input, expect, 524))
