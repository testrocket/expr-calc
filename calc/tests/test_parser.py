import unittest

from calc.main import parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.expr = "a + 2 * sin(2 - 1) + b"

    def test_parse1(self):
        result = str(parser.parse_rpn(self.expr))
        assert result == "[a, 2, 2, 1, -, sin, *, +, b, +]", "Incorrect parse result: %s" % result

