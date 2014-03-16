import unittest

from calc.main import parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.expr = "1 + 2 * (2 - 1)"

    def test_parse1(self):
        result = str(parser.parse_rpn(self.expr))
        assert result == "[1, 2, 2, 1, -, *, +]", "Incorrect parse result: %s" % result

    def test_parse2(self):
        result = str(parser.parse_rpn(self.expr))
        assert result != "[1, 2, 2, 1, *, -, +]", "Incorrect parse result: %s" % result