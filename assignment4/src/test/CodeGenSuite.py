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
    #     expect = "falsetruefalsefalsetruetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))

    # def test_26(self):
    #     input = """
    #     i: integer = 1;
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
    #     y: array[10, 10] of float = {{2, 3}, {1}, {5}};
    #     main: function void() {
    #         x[0, 2] = 99;
    #         y[0, 2] = 99;
    #         printInteger(x[0, 2] + x[0, 0]);
    #         writeFloat(y[0, 2]);
    #     }
    #     """
    #     expect = "10199.0"
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

    # def test_34(self):
    #     input = """
    #     main: function void() {
    #         if (1 > 2) {
    #             printBoolean(true);
    #         } else {
    #             printBoolean(false);
    #         }
    #         printBoolean(false);
    #     }
    #     """
    #     expect = "falsefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))

    # def test_35(self):
    #     input = """
    #     main: function void() {
    #         if (!(1 > 2)) {
    #             printBoolean(true);
    #         } else {
    #             printBoolean(false);
    #         }
    #         printBoolean(false);
    #     }
    #     """
    #     expect = "truefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))

    # def test_36(self):
    #     input = """
    #     main: function void() {
    #         i: integer = 1;
    #         x: array[10, 10] of integer;
    #         if (i % 2 == 0) {
    #             x[i, 0] = i;
    #         } else {
    #             x[0, i] = i + 1;
    #         }
    #         printInteger(x[0, i]);
    #     }
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))

    # def test_37(self):
    #     input = """
    #     main: function void() {
    #         i: integer = 1;
    #         x: array[10, 10] of integer;
    #         if (i % 2 != 0) {
    #             x[i, 0] = i;
    #         } else {
    #             x[0, i] = i + 1;
    #         }
    #         printInteger(x[i, 0]);
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))

    # def test_38(self):
    #     input = """
    #     main: function void() {
    #         i: integer = 5;
    #         x: array[10, 10] of integer = {{101, 202}, {i}};
    #         printInteger(x[1, 0]);
    #         if (i % 2 != 0) {
    #             x[i, 0] = i;
    #         }  else {
    #             x[0, i] = i + 1;
    #         }
    #         printInteger(x[i, 0]);
    #     }
    #     """
    #     expect = "55"
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))

    # def test_39(self):
    #     input = """
    #     main: function void() {
    #         i: integer;
    #         for (i = 1, i < 10, i+1) {
    #             printInteger(i);
    #         }
    #     }
    #     """
    #     expect = "123456789"
    #     self.assertTrue(TestCodeGen.test(input, expect, 539))

    # def test_40(self):
    #     input = """
    #     main: function void() {
    #         i, j: integer;
    #         for (i = 1, i < 2, i+1) {
    #             for (j = 1, j < 2, j+1) {
    #                 if (i + j >= 2) {
    #                     printInteger(i+j);
    #                 } else {
    #                     printInteger(i-j);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 540))

    # def test_41(self):
    #     input = """
    #     main: function void() {
    #         for (i = 1, i < 2, i+1) {
    #             for (j = 1, j < 2, j+1) {
    #                 if (i + j >= 2) {
    #                     printInteger(i+j);
    #                 } else {
    #                     printInteger(i-j);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 541))

    # def test_42(self):
    #     input = """
    #     main: function void() {
    #         for (i = 1, i < 2.0, i+1) {
    #             for (j = 1, j < 2.0, j+1) {
    #                 if (i + j >= 2.0) {
    #                     printInteger(i+j);
    #                 } else {
    #                     printInteger(i-j);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 542))

    # def test_43(self):
    #     input = """
    #     main: function void() {
    #         for (i = 1, i < 20, i+1) {
    #             printInteger(i);
    #             break;
    #         }
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 543))

    # def test_44(self):
    #     input = """
    #     main: function void() {
    #         i, j: integer;
    #         for (i = 1, i < 20, i+1) {
    #             for (j = 1, j < 20, j+1) {
    #                 if (i + j >= 2) {
    #                     printInteger(i+j);
    #                     break;
    #                 } else {
    #                     printInteger(i-j);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = "234567891011121314151617181920"
    #     self.assertTrue(TestCodeGen.test(input, expect, 544))

    # def test_45(self):
    #     input = """
    #     main: function void() {
    #         i, j: integer;
    #         for (i = 1, i < 5, i+1) {
    #             for (j = 1, j < 5, j+1) {
    #                 continue;
    #                 if (i + j >= 2) {
    #                     printInteger(i+j);
    #                 } else {
    #                     printInteger(i-j);
    #                 }
    #             }
    #             printInteger(i);
    #         }
    #     }
    #     """
    #     expect = "1234"
    #     self.assertTrue(TestCodeGen.test(input, expect, 545))

    # def test_46(self):
    #     input = """
    #     main: function void() {
    #         i, j: integer;
    #         for (i = 1, i < 5, i+1) {
    #             for (j = 1, j < 5, j+1) {
    #                 if (i + j >= 2) {
    #                     printInteger(i+j);
    #                     return;
    #                 } else {
    #                     printInteger(i-j);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 546))

    # def test_47(self):
    #     input = """
    #     main: function void() {
    #         i: integer = 0;
    #         while (i != 20) {
    #             i = i + 1;
    #         }
    #         printInteger(i);
    #     }
    #     """
    #     expect = "20"
    #     self.assertTrue(TestCodeGen.test(input, expect, 547))

    # def test_48(self):
    #     input = """
    #     main: function void() {
    #         i: integer = 0;
    #         while (i != 20) {
    #             if (i == 10) {
    #                 i = 100;
    #                 break;
    #             }
    #             i = i + 1;
    #         }
    #         printInteger(i);
    #     }
    #     """
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input, expect, 548))

    # def test_49(self):
    #     input = """
    #     main: function void() {
    #         i, nE: integer = 0, 10;
    #         do {
    #             for (i = 0, i < nE, i+1)
    #                 if (nE == 10 + 5)
    #                     break;
    #                 else
    #                     nE = nE + 1;
    #             break;
    #         } while(true);
    #         printInteger(i);
    #     }
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 549))

    # def test_50(self):
    #     input = """
    #     main: function void() {
    #         i, nE: integer = 0, 10;
    #         do {
    #             for (i = 0, i < nE, i+1)
    #                 if (nE == 10 + 5)
    #                     continue;
    #                 else
    #                     nE = nE + 1;
    #             break;
    #         } while(true);
    #         printInteger(nE);
    #     }
    #     """
    #     expect = "15"
    #     self.assertTrue(TestCodeGen.test(input, expect, 550))

    # def test_51(self):
    #     input = """
    #     main: function void() {
    #         i: integer = 0;
    #         do{
    #             j : integer = 0;
    #             while (j < 20) {
    #                 if (i + j >= 20) {
    #                     break;
    #                 } else {
    #                     j = j + 1;
    #                 }
    #             }
    #             printInteger(j);
    #             i = i + 1;
    #         }while(i < 10);
    #     }
    #         """
    #     expect = "20191817161514131211"
    #     self.assertTrue(TestCodeGen.test(input, expect, 551))

    # def test_52(self):
    #     input = """
    #     fact: function integer (n: integer) {
    #         if (n == 0) return 1;
    #         else return n;
    #     }
    #     main: function void() {
    #         delta: integer = fact(3);
    #         printInteger(delta);
    #     }
    #         """
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input, expect, 552))

    # def test_53(self):
    #     input = """
    #     x: integer = 65;
    #     fact: function integer (n: integer) {
    #         if (n == 0) return 1;
    #         else return n * fact(n - 1);
    #     }
    #     inc: function void(n: integer, delta: integer) {
    #         n = n + delta;
    #         printInteger(n);
    #     }
    #     main: function void() {
    #         delta: integer = fact(3);
    #         inc(x, delta);
    #     }
    #         """
    #     expect = "71"
    #     self.assertTrue(TestCodeGen.test(input, expect, 553))

    # def test_54(self):
    #     input = """
    #     main: function void() {
    #         for (i = 1, i < 10, i+1) {
    #             printInteger(i);
    #             return;
    #         }
    #     }
    #         """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 554))

    # def test_55(self):
    #     input = """
    #     inc: function integer(n: integer, delta: integer) {
    #         n = n + delta;
    #         for (i = 1, i < 10, i+1) {
    #             return i;
    #         }
    #         return 10;
    #     }
    #     main: function void() {
    #         printInteger(inc(1, 1));
    #     }
    #         """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 555))

    # def test_56(self):
    #     input = """
    #     inc: function integer(n: integer, delta: integer) {
    #         n = n + delta;
    #         for (i = 1, i < 10, i+1) {
    #             while(n < 10) {
    #                 return i;
    #             }
    #         }
    #         return 10;
    #     }
    #     main: function void() {
    #         printInteger(inc(1, 1));
    #        }
    #     }
    #         """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 556))

    # def test_57(self):
    #     input = """
    #     inc: function float(n: integer, delta: integer) {
    #         n = n + delta;
    #         for (i = 1, i < n, i+1) {
    #             for (j = 1, j < n, j+1) {
    #                 if (i + j >= 2) {
    #                     return i + j;
    #                 } else {
    #                     printInteger(i-j);
    #                 }
    #             }
    #         }
    #         return 0;
    #     }
    #     main: function void() {
    #         writeFloat(inc(2, 2));
    #     }
    #     """
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 557))

    # def test_58(self):
    #     input = """
    #     main: function void() {
    #         i: integer = 1;
    #         while(i < 10)
    #             return;
    #     }
    #         """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 558))

    # def test_59(self):
    #     input = """
    #     arr: array[100] of integer;
    #     checkDuplicate: function boolean(ar: array[100] of integer, size: integer) {
    #       if (size <= 1)
    #         return true;
    #       less, greater: array[100] of integer;
    #       greater_size, less_size: integer  = 0, 0;

    #       for (i = 1, i < size, i+1) {
    #         if (ar[i] == ar[0]) {
    #           return false;
    #         }

    #         if (ar[i] < ar[0]) {
    #           less[less_size] = ar[i];
    #           less_size = less_size + 1;
    #         } else {
    #           greater[greater_size] = ar[i];
    #           greater_size = greater_size + 1;
    #         }
    #       }

    #       return checkDuplicate(less, less_size) && checkDuplicate(greater, greater_size);
    #     }

    #     main: function void() {
    #         printBoolean(checkDuplicate(arr, 100));
    #     }
    #         """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 559))

    # def test_60(self):
    #     input = """
    #     less_zero: boolean = false;
    #     c: integer = 0;

    #     printPattern: function void(n: integer) {
    #       if (n <= 0) {
    #         less_zero = true;
    #       }

    #       if (less_zero) {
    #         c = c - 1;
    #         if (c == -1) {
    #             printInteger(n);
    #             return;
    #         }
    #         printPattern(n + 5);
    #       } else {
    #         c = c + 1;
    #         printPattern(n - 5);
    #       }
    #     }
    #     main: function void() {
    #         printPattern(5);
    #     }
    #         """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 560))

    # def test_61(self):
    #     input = """
    #     checkElementsUniqueness: function boolean (arr: array[100] of integer, n: integer) {
    #       if ((n > 1000) || (n < 0))
    #         return false;
    #       for (i = 0, i < n - 1, i+1) {
    #         for (j = i + 1, j < n, j+1) {
    #           if (arr[i] == arr[j])  {
    #             return false;
    #           }

    #         }
    #       }
    #       return true;
    #     }

    #     main: function void() {
    #         arr: array [6] of integer = {1, 91, 0, -100, 100, 200};
    #         if (checkElementsUniqueness(arr, 6)) printString("Correct!");
    #         else printString("Wrong!");
    #     }
    #         """
    #     expect = "Correct!"
    #     self.assertTrue(TestCodeGen.test(input, expect, 561))

    # def test_62(self):
    #     input = """
    #     checkElementsUniqueness: function boolean (arr: array[100] of integer, n: integer) {
    #       if ((n > 1000) || (n < 0))
    #         return false;
    #       for (i = 0, i < n - 1, i+1) {
    #         for (j = i + 1, j < n, j+1) {
    #           if (arr[i] == arr[j])  {
    #             return false;
    #           }

    #         }
    #       }
    #       return true;
    #     }

    #     main: function void() {
    #         arr: array [6] of integer = {1, 91, 0, -100, 100, 1};
    #         if (checkElementsUniqueness(arr, 6)) printString("Correct!");
    #         else printString("Wrong!");
    #     }
    #         """
    #     expect = "Wrong!"
    #     self.assertTrue(TestCodeGen.test(input, expect, 562))

    # def test_63(self):
    #     input = """
    #     checkElementsUniqueness: function boolean (arr: array[100] of integer, n: integer) {
    #       if ((n > 1000) || (n < 0))
    #         return false;
    #       for (i = 0, i < n - 1, i+1) {
    #         for (j = i + 1, j < n, j+1) {
    #           if (arr[i] == arr[j])  {
    #             return false;
    #           }

    #         }
    #       }
    #       return true;
    #     }

    #     main: function void() {
    #         arr: array [6] of integer = {1, 91, 0, -100, 100, 1};
    #         if (checkElementsUniqueness(arr, 6)) printString("Correct!");
    #         else printString("Wrong!");
    #     }
    #         """
    #     expect = "Wrong!"
    #     self.assertTrue(TestCodeGen.test(input, expect, 563))

    # def test_64(self):
    #     input = """
    #     main : function void () {
    #         f : array [5] of string = {"kiet", "", ""};
    #         printString(f[0]);
    #     }
    #         """
    #     expect = "kiet"
    #     self.assertTrue(TestCodeGen.test(input, expect, 564))

    # def test_65(self):
    #     input = """
    #     main : function void () {
    #         f : array [5] of boolean = {true, false, true};
    #         printBoolean(f[0]);
    #     }
    #         """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 565))

    # def test_66(self):
    #     input = """
    #     main: function void() {
    #         arr   : array [3] of string = {"Cao", "Hoang", "Kiet"};
    #         arr[0] = (arr[0]::arr[1])::arr[2];
    #         printString(arr[0]);
    #     }
    #             """
    #     expect = "CaoHoangKiet"
    #     self.assertTrue(TestCodeGen.test(input, expect, 566))

    # def test_67(self):
    #     input = """
    #     main: function void() {
    #         f : array [5] of boolean = {true, false, true};
    #         printBoolean(f[0] && f[1] && f[2]);
    #     }
    #             """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 567))

    # def test_68(self):
    #     input = """
    #     foo1: function string (inherit c: string, d: float) {
    #         return "foo1";
    #     }
    #     foo: function string (inherit a: string, b: float) inherit foo1 {
    #         super("World!", 123.0);
    #         printString(a::c);
    #         return "foo";
    #     }
    #     main : function void () {
    #         foo("Hello", 1.1);
    #     }
    #         """
    #     expect = "HelloWorld!"
    #     self.assertTrue(TestCodeGen.test(input, expect, 568))

    # def test_68(self):
    #     input = """
    #     foo1: function string (inherit c: string, d: float) {
    #         return "foo1";
    #     }
    #     foo: function string (inherit a: string, b: string) inherit foo1 {
    #         super("World!"::b, 123.0);
    #         return "foo";
    #     }
    #     bar: function void (inherit x: integer, inherit y: string) inherit foo {
    #         super("Hello", "Kiet");
    #         printString(c);
    #     }
    #     main : function void () {
    #         bar(1, "hello");
    #     }
    #         """
    #     expect = "World!Kiet"
    #     self.assertTrue(TestCodeGen.test(input, expect, 568))

    # def test_69(self):
    #     input = """
    #     foo1: function string (inherit c: string, d: float) {
    #         return "foo1";
    #     }
    #     foo: function string (inherit a: string, b: string) inherit foo1 {
    #         super("World!"::b, 123.0);
    #         return "foo";
    #     }
    #     bar: function void (inherit x: integer, inherit y: string) inherit foo {
    #         super("Hello", "Kiet");
    #         printString(a::c);
    #     }
    #     main : function void () {
    #         bar(1, "hello");
    #     }
    #         """
    #     expect = "HelloWorld!Kiet"
    #     self.assertTrue(TestCodeGen.test(input, expect, 569))

    #     def test_70(self):
    #         input = """
    #         foo1: function string (inherit c: string, d: float) {
    #             return "foo1";
    #         }
    #         foo: function string (inherit a: string, b: string) inherit foo1 {
    #             super("World!"::b, 123.0);
    #             return "foo";
    #         }
    #         bar: function void (inherit x: integer, inherit y: string) inherit foo {
    #             super("Hello", "Kiet");
    #             b: integer = 3;
    #             printString((a::c)::"\\n");
    #             printInteger(b + x);
    #         }
    #         main : function void () {
    #             bar(1, "hello");
    #         }
    #             """
    #         expect = """HelloWorld!Kiet
    # 4"""
    #         self.assertTrue(TestCodeGen.test(input, expect, 570))

    # def test_71(self):
    #     input = """
    #     inc: function integer (inherit a: integer, b: integer)
    #     {
    #         while (a!=0)
    #             a = a - 1;
    #         do {
    #             a = b + 1;
    #         }
    #         while (a <= b);
    #         return a;
    #     }
    #     main: function void() inherit inc {
    #         super(3, 10);
    #         printInteger(a + inc(5, 10));
    #     }
    #         """
    #     expect = "14"
    #     self.assertTrue(TestCodeGen.test(input, expect, 571))

    # def test_72(self):
    #     input = """
    #     haha: function integer(inherit x: integer){
    #         return 1;
    #     }

    #     haha1: function float() inherit haha{
    #         super(100);
    #         return 1;
    #     }
    #     main: function void() inherit haha1 {
    #         printInteger(x);
    #     }
    #         """
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input, expect, 572))

    # def test_72(self):
    #     input = """
    #     foo: function string (a: string, b: float) {
    #         d: string = a;
    #         f : array [5] of string = {"Yooooo!", "Loooo"};
    #         return (f[0]::f[1])::d;
    #     }
    #     bar: function void (inherit out a: float, inherit out b: string) inherit foo {
    #         super("Hello", 123);
    #         for (i = 1, i < 10, i + 1)
    #         {
    #             writeFloat(a);
    #         }
    #         if (a==2)
    #             return;
    #     }
    #     main: function void() {
    #         bar(5, "yep");
    #         printString(foo("Friend", 1));
    #     }
    #         """
    #     expect = "5.05.05.05.05.05.05.05.05.0Yooooo!LooooFriend"
    #     self.assertTrue(TestCodeGen.test(input, expect, 572))

    # def test_73(self):
    #     input = """
    #     foo1: function integer (a: string, b: integer, c: float, d: boolean) {
    #         return b + 1;
    #     }
    #     foo: function string (a: string, inherit b: integer, inherit c: float, d: boolean) inherit foo1{
    #         super("Hello"::a, 134, 12.0, false);
    #         f : array [5] of string = {"a"};
    #         return f[0];
    #     }
    #     bar: function void (inherit a: integer, x: string) inherit foo {
    #         super("Hello"::x, 123, 11.0, true);
    #         writeFloat((a + b) + c);
    #     }
    #     main: function void() {
    #         bar(10, "World!");
    #     }
    # """
    #     expect = "144.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 573))

    # def test_74(self):
    #     input = """
    #     foo1: function integer (a: string, b: integer, inherit c: float, inherit d: boolean) {
    #         return b + 1;
    #     }
    #     foo: function string (a: string, inherit b: integer) inherit foo1{
    #         super("Hello"::a, 134, 12.0, false);
    #         f : array [5] of string = {"a"};
    #         return f[0];
    #     }
    #     bar: function void (inherit a: integer, x: string) inherit foo {
    #         super("Hello"::x, 123);
    #         writeFloat((a + b) + c);
    #     }
    #     main: function void() {
    #         bar(10, "World!");
    #     }
    # """
    #     expect = "145.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 574))

    # def test_75(self):
    #     input = """
    #     foo1: function integer (a: string, b: integer, inherit c: float, inherit d: boolean) {
    #         printString(a);
    #         return b + 1;
    #     }
    #     foo: function string (a: string, inherit b: integer) inherit foo1{
    #         super("Hello"::a, 134, 12.0, false);
    #         f : array [5] of string = {"a"};
    #         return f[0];
    #     }
    #     bar: function void (inherit a: integer, x: string) inherit foo {
    #         super("Hello"::x, 123);
    #         writeFloat((a + b) + c);
    #     }
    #     main: function void() {
    #         bar(10, "World!");
    #         printInteger(foo1("", 1, 1.0, false));
    #     }
    # """
    #     expect = "145.02"
    #     self.assertTrue(TestCodeGen.test(input, expect, 575))

    # def test_76(self):
    #     input = """
    #     foo1: function integer (a: string, b: integer, inherit c: float, inherit d: boolean) {
    #         printString(a);
    #         return b + 1;
    #     }
    #     foo: function string (a: string, inherit b: integer) inherit foo1{
    #         super("Hello"::a, 134, 12.0, false);
    #         writeFloat(c);
    #         f : array [5] of string = {"a"};
    #         return f[0]::a;
    #     }
    #     bar: function void (inherit a: integer, x: string) inherit foo {
    #         super("Hello"::x, 123);
    #         writeFloat((a + b) + c);
    #     }
    #     main: function void() {
    #         bar(10, "World!");
    #         printString(foo("", 1));
    #         printInteger(foo1("", 1, 1.0, false));
    #     }
    # """
    #     expect = "145.012.0a2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 576))

    # def test_76(self):
    #     input = """
    #     foo1: function integer (a: string, b: integer, inherit c: float, inherit d: boolean) {
    #         printString(a);
    #         return b + 1;
    #     }
    #     foo: function string (a: string, inherit b: integer) inherit foo1{
    #         super("Hello"::a, 134, 12.0, false);
    #         writeFloat(c);
    #         f : array [5] of string = {"a"};
    #         return f[0]::a;
    #     }
    #     bar: function void (inherit a: integer, x: string) inherit foo {
    #         super("Hello"::x, 123);
    #         writeFloat((a + b) + c);
    #     }
    #     main: function void() {
    #         bar(10, "World!");
    #         printString(foo("", 1));
    #         printInteger(foo1("", 1, 1.0, false));
    #     }
    # """
    #     expect = "145.012.0a2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_70(self):
        input = r"""
        foo: function string (a: integer, b: string) {
            f : array [5] of string = {b};
            return f[0];
        }
        foo1: function string (a: string, b: integer) inherit foo{
            super(b, a);
            f : array [5] of string = {a};
            return f[0];
        }
        bar: function void (inherit out a: integer, inherit out b: string) inherit foo1 {
            super("Hello"::b, a);
            for (i = 1, i < 10, i + 1)
            {
                writeFloat(a);
            }
            if (a==2)
                return;
            // printString(a);
            //printString(foo("Hello", 1.2312));
        }
        main: function void() {
            bar(10, "World!");
        }
    """
        expect = "[]"
        self.assertTrue(TestCodeGen.test(input, expect, 570))
