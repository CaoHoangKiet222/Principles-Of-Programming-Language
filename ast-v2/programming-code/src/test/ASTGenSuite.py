import unittest
from TestUtils import TestAST


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """a := b := 4"""
        expect = "Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))"
        self.assertTrue(TestAST.test(input, expect, 100))

    def test_2(self):
        input = """a >= b"""
        expect = "Binary(>=,Id(a),Id(b))"
        self.assertTrue(TestAST.test(input, expect, 101))

    def test_3(self):
        input = """(a := c) >= b"""
        expect = "Binary(>=,Binary(:=,Id(a),Id(c)),Id(b))"
        self.assertTrue(TestAST.test(input, expect, 102))

    def test_4(self):
        input = """(a >= c) or (a >= b)"""
        expect = "Binary(or,Binary(>=,Id(a),Id(c)),Binary(>=,Id(a),Id(b)))"
        self.assertTrue(TestAST.test(input, expect, 103))
