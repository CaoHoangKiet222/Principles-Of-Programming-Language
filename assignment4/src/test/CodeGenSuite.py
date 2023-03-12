import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_1(self):
        input = """
        x, y: integer;
        main: function void() {
            x: integer;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 501))
