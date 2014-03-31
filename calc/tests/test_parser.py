import unittest

from calc.main import parser

class TestParser(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse1(self):
        result = str(parser.parse_rpn("a + 2 * sin(2 - 1) + b"))
        assert result == "[a, 2, 2, 1, -, sin, *, +, b, +]", "Incorrect parse result: %s" % result

    def test_parse2(self):
        result = str(parser.parse_rpn("a = 1 + 2 * 4"))
        assert result == "[a, 1, 2, 4, *, +, =]", "Incorrect parse result: %s" % result

    def test_parse3(self):
        result = str(parser.parse_rpn("a = cos( 2 + 4) * 2"))
        assert result == "[a, 2, 4, +, cos, 2, *, =]", "Incorrect parse result: %s" % result

    def test_parse4(self):
        result = str(parser.parse_rpn("a = cos(2 + 4) ^ 2 + 2"))
        assert result == "[a, 2, 4, +, cos, 2, ^, 2, +, =]", "Incorrect parse result: %s" % result
