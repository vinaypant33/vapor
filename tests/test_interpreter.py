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

    def test_unary_minus(self):
        self.assertEqual(value_of("-5 + 2"), -3)
        self.assertEqual(value_of("--5"), 5)
        self.assertEqual(value_of("+5"), 5)

    def test_division_by_zero(self):
        with self.assertRaises(VaporRuntimeError) as context:
            value_of("1 / 0")
        self.assertIn("Division by zero", str(context.exception))

    def test_modulo_by_zero(self):
        with self.assertRaises(VaporRuntimeError):
            value_of("1 % 0")


class TestStrings(unittest.TestCase):
    def test_string_value(self):
        self.assertEqual(value_of('"hello"'), "hello")

    def test_join_strings(self):
        self.assertEqual(value_of('"Va" + "por"'), "Vapor")

    def test_join_string_and_number(self):
        self.assertEqual(value_of('"Age: " + 30'), "Age: 30")
        self.assertEqual(value_of('1 + "st"'), "1st")

    def test_cannot_subtract_strings(self):
        with self.assertRaises(VaporRuntimeError) as context:
            value_of('"a" - "b"')
        self.assertIn("Cannot use '-'", str(context.exception))

    def test_cannot_multiply_string(self):
        with self.assertRaises(VaporRuntimeError):
            value_of('"ab" * 3')

    def test_cannot_negate_string(self):
        with self.assertRaises(VaporRuntimeError):
            value_of('-"text"')


class TestVariables(unittest.TestCase):
    def test_declare_and_use(self):
        self.assertEqual(value_of("let_it x = 4\nx * x"), 16)

    def test_reassign(self):
        self.assertEqual(value_of("let_it x = 1\nx = x + 1\nx = x + 1\nx"), 3)
