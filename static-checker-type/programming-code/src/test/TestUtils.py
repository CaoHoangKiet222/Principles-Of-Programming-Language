import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
if not './main/bkool/parser/' in sys.path:
    sys.path.append('./main/bkool/parser/')
if os.path.isdir('../target/main/bkool/parser') and not '../target/main/bkool/parser/' in sys.path:
    sys.path.append('../target/main/bkool/parser/')
from StaticCheck import StaticChecker
from StaticError import *
import subprocess

JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestChecker:
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            # inputfile = TestUtil.makeSource(input, num)
            # lexer = Lexer(inputfile)
            # tokens = CommonTokenStream(lexer)
            # parser = Parser(tokens)
            # tree = parser.program()
            # asttree = ASTGeneration().visit(tree)
            pass
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input
        TestChecker.check(SOL_DIR, asttree, num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            dest.write(str(res))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()
