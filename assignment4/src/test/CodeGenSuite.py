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
    #     x: integer = 12_1111;
    #     main: function void() {
    #         printInteger(x);
    #     }
    #     """
    #     expect = "121111"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    # def test_6(self):
    #     input = """
    #     x, y: float = 1, 102332.23423;
    #     main: function void() {
    #         writeFloat(x);
    #         writeFloat(y);
    #     }
    #     """
    #     expect = "1.0102332.234"
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
    #         printString("hello"::"world");
    #         printString(("hello"::"world")::" with kiet");
    #         printString(("hello"::"world")::(" with kiet"::" cao hoang"));
    #     }
    #     """
    #     expect = "helloworldhelloworld with kiethelloworld with kiet cao hoang"
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
    #         printBoolean((2.0 > 1) && (3 < 4));
    #     }
    #     """
    #     expect = "true"
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

    # def test_24(self):
    #     input = """
    #     main: function void() {
    #         printInteger(-1);
    #         printInteger(-1 + 2);
    #     }
    #     """
    #     expect = "-11"
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))

    # def test_25(self):
    #     input = """
    #     main: function void() {
    #         printBoolean(1_1.5*2 + 2 - 5_2.3*2.1 > 3*5 + 2_2*3/2 - 4*7.2/14 + 1);
    #         printBoolean(1_1.5*2 + 2 - 5_2.3*2.1 < 3*5 + 2_2*3/2 - 4*7.2/14 + 1);
    #         printBoolean(1_1.5*2 + 2 - 5_2.3*2.1 == 3*5 + 2_2*3/2 - 4*7.2/14 + 1);
    #         printBoolean(1_1.5*2 + 2 - 5_2.3*2.1 >= 3*5 + 2_2*3/2 - 4*7.2/14 + 1);
    #         printBoolean(1_1.5*2 + 2 - 5_2.3*2.1 <= 3*5 + 2_2*3/2 - 4*7.2/14 + 1);
    #         printBoolean(1_1.5*2 + 2 - 5_2.3*2.1 != 3*5 + 2_2*3/2 - 4*7.2/14 + 1);
    #     }
    #     """
    #     expect = "falsetruetruefalsetruetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))

    # def test_26(self):
    #     input = """
    #     a: array[10] of integer = {1, 2, 3, 4};
    #     b: array[10] of integer;
    #     main: function void() {
    #         c: array[10] of integer = {1, 2, 3, 4};
    #         d: array[10] of integer = {2, 3, 4, 5};
    #         printInteger(a[2] + b[1] + c[0] + d[5]);
    #     }
    #     """
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))

    # def test_27(self):
    #     input = """
    #     arr1 : array [1, 2] of integer = {{1, 3}};
    #     arr2 : array [3, 2] of integer = {{1}, {123, 1238, 6}, {5, 0}};
    #     main: function void() {
    #         arr3 : array [2, 3, 2] of integer = {{{1, 3}, {12, 13}, {123, 321}}, {{2, 41}, {123, 123}, {923, 32}}};
    #         printInteger(arr1[0+0, 1]);
    #         printInteger(arr2[0+2, 1]);
    #         printInteger(arr2[1-(-1), 1]);
    #         printInteger(arr2[4%4, 1]);
    #         printInteger(arr3[1, 1, 1]);
    #     }
    #     """
    #     expect = "3000123"
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))

    # def test_28(self):
    #     input = """
    #     x: integer;
    #     main: function void() {
    #         x = 1;
    #         printInteger(x);
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))

    # def test_29(self):
    #     input = """
    #     x: string;
    #     main: function void() {
    #         x = "hello";
    #         printString(x);
    #     }
    #     """
    #     expect = "hello"
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))

    # def test_30(self):
    #     input = """
    #     x: boolean;
    #     main: function void() {
    #         x = true;
    #         printBoolean(x);
    #     }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))

    # def test_31(self):
    #     input = """
    #     x: array[10] of integer;
    #     main: function void() {
    #         x[0] = 1;
    #         x[2] = 100;
    #         printInteger(x[0] + x[2]);
    #     }
    #     """
    #     expect = "101"
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))

    # def test_32(self):
    #     input = """
    #     x: array[10, 10] of integer = {{2, 3}, {1}, {5}};
    #     main: function void() {
    #         x[0, 2] = 99;
    #         printInteger(x[0, 2] + x[0, 0]);
    #     }
    #     """
    #     expect = "101"
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))

    # def test_32(self):
    #     input = """
    #     x: array[10, 10] of float = {{2, 3}, {1}, {5}};
    #     main: function void() {
    #         x[0, 2] = 99;
    #         writeFloat(x[0, 2]);
    #     }
    #     """
    #     expect = "99.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))

    # def test_33(self):
    #     input = """
    #     main: function void() {
    #         if (1 < 2) {
    #             printBoolean(true);
    #         } else {
    #             printBoolean(false);
    #         }
    #     }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_34(self):
        input = """
        main: function void() {
            if (1 > 2) {
                printBoolean(true);
                // return;
            } else {
                printBoolean(false);
                return;
            }
            printBoolean(false);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 534))
