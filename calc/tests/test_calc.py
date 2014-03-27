import unittest

from calc import calc

class TestParser(unittest.TestCase):
    def setUp(self):
        pass

    def test_calculate1(self):
        result = calc.calculate("1 + 2")
        assert result == 3, "Incorrect calculation result: %s" % result

    def test_calculate2(self):
        result = calc.calculate("1 + 2 * 3")
        assert result == 7, "Incorrect calculation result: %s" % result

    def test_calculate3(self):
        result = calc.calculate("(1 + 2) * 3")
        assert result == 9, "Incorrect calculation result: %s" % result

    def test_calculate4(self):
        result = calc.calculate("1 + sin(rad(90))")
        assert result == 2, "Incorrect calculation result: %s" % result

    def test_calculate5(self):
        result = calc.calculate("1 + cos(rad(90))")
        assert result == 1, "Incorrect calculation result: %s" % result

    def test_calculate6(self):
        result = calc.calculate("2 ^ 3")
        assert result == 8, "Incorrect calculation result: %s" % result

    def test_calculate7(self):
        result = calc.calculate("2 ^ 3 * 2 + 10")
        assert result == 26, "Incorrect calculation result: %s" % result

    def test_calculate8(self):
        result = calc.calculate("2 * int(2 + 1.9)")
        assert result == 6, "Incorrect calculation result: %s" % result

    def test_calculate9(self):
        result = calc.calculate("int(1.3 + 1.9) ^ int(2 + 1.9)")
        assert result == 27, "Incorrect calculation result: %s" % result
