import unittest
from calc.main import tokens

class TokenTest(unittest.TestCase):

    def setUp(self):
        self.expr = "3 * (2 - 1)"

    def test_token_count(self):
        result = tokens.tokenize(self.expr)
        assert len(result) == 7, "Incorrect number of tokens, expected 7, got %s" % len(result)

    def test_token_type_int(self):
        result = tokens.tokenize("2")
        assert result[0].ttype == tokens.Token.INT, "Expected INT type, got: %s" % result[0].ttype

    def test_token_value_int(self):
        result = tokens.tokenize("123")
        assert result[0].value == "123", "Expected value 123, got: %s" % result[0].value

    def test_token_type_double(self):
        result = tokens.tokenize("2.0")
        assert result[0].ttype == tokens.Token.DOUBLE, "Expected DOUBLE type, got: %s" % result[0].ttype

    def test_token_value_double(self):
        result = tokens.tokenize("123.987")
        assert result[0].value == "123.987", "Expected value 123.987, got: %s" % result[0].value

    def test_token_type_op_add(self):
        result = tokens.tokenize("+")
        assert result[0].ttype == tokens.Token.OP_ADD, "Expected OP_ADD type, got: %s" % result[0].ttype

    def test_token_type_paren_left(self):
        result = tokens.tokenize("(")
        assert result[0].ttype == tokens.Token.PAREN_LEFT, "Expected PAREN_LEFT type, got: %s" % result[0].ttype
