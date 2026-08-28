import unittest

from vapor.errors import LexerError
from vapor.lexer import Lexer
from vapor.tokens import (
    COMMA,
    EOF,
    EQUAL,
    IDENTIFIER,
    LET_IT,
    LPAREN,
    MINUS,
    NEWLINE,
    NUMBER,
    PERCENT,
    PLUS,
    PRINT,
    RPAREN,
    SLASH,
    STAR,
    STRING,
)


def token_types(source):
    return [token.type for token in Lexer(source).get_tokens()]


def token_values(source):
    return [token.value for token in Lexer(source).get_tokens()]


class TestBasics(unittest.TestCase):
    def test_empty_source_gives_only_eof(self):
        self.assertEqual(token_types(""), [EOF])

    def test_whitespace_is_skipped(self):
        self.assertEqual(token_types("   \t  "), [EOF])


class TestNumbers(unittest.TestCase):
    def test_whole_number(self):
        tokens = Lexer("42").get_tokens()
        self.assertEqual(tokens[0].type, NUMBER)
        self.assertEqual(tokens[0].value, 42)
        self.assertIsInstance(tokens[0].value, int)

    def test_decimal_number(self):
        tokens = Lexer("3.14").get_tokens()
        self.assertEqual(tokens[0].value, 3.14)
        self.assertIsInstance(tokens[0].value, float)

    def test_two_decimal_points_is_an_error(self):
        with self.assertRaises(LexerError):
            Lexer("1.2.3").get_tokens()

    def test_trailing_decimal_point_is_an_error(self):
        with self.assertRaises(LexerError):
            Lexer("5.").get_tokens()


class TestNamesAndKeywords(unittest.TestCase):
    def test_keywords(self):
        self.assertEqual(token_types("let_it print"), [LET_IT, PRINT, EOF])

    def test_identifier(self):
        tokens = Lexer("total_2").get_tokens()
        self.assertEqual(tokens[0].type, IDENTIFIER)
        self.assertEqual(tokens[0].value, "total_2")

    def test_identifier_may_start_with_underscore(self):
        self.assertEqual(token_types("_hidden"), [IDENTIFIER, EOF])
