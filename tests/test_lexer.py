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
