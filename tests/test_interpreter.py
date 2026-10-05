import io
import unittest

from vapor.environment import Environment
from vapor.errors import VaporRuntimeError
from vapor.runner import run_source


def output_of(source):
    buffer = io.StringIO()
    run_source(source, output=buffer)
    return buffer.getvalue()


def value_of(source):
    return run_source(source, output=io.StringIO())


class TestArithmetic(unittest.TestCase):
    def test_addition_and_subtraction(self):
        self.assertEqual(value_of("10 + 5 - 3"), 12)

    def test_precedence(self):
        self.assertEqual(value_of("2 + 3 * 4"), 14)
        self.assertEqual(value_of("(2 + 3) * 4"), 20)

    def test_whole_division_stays_whole(self):
        result = value_of("10 / 2")
        self.assertEqual(result, 5)
        self.assertIsInstance(result, int)

    def test_division_with_remainder_gives_decimal(self):
        self.assertEqual(value_of("7 / 2"), 3.5)

    def test_modulo(self):
        self.assertEqual(value_of("17 % 5"), 2)

    def test_decimals(self):
        self.assertAlmostEqual(value_of("0.5 * 3"), 1.5)
