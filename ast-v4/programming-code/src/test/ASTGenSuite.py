import unittest
from TestUtils import TestAST


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = "real [-3..0][-10..-1]"
        expect = "ArrayType(UnionType(RangeType(-3,0),RangeType(-10,-1)),FloatType)"
        self.assertTrue(TestAST.test(input, expect, 100))

    def test_2(self):
        input = "integer[1..3]"
        expect = "ArrayType(RangeType(1,3),IntType)"
        self.assertTrue(TestAST.test(input, expect, 101))

    def test_3(self):
        input = """integer [1..100][-5..20][100..3000]"""
        expect = "ArrayType(UnionType(UnionType(RangeType(1,100),RangeType(-5,20)),RangeType(100,3000)),IntType)"
        self.assertTrue(TestAST.test(input, expect, 102))
