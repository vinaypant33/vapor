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

    def test_keyword_prefix_is_still_an_identifier(self):
        self.assertEqual(token_types("printer"), [IDENTIFIER, EOF])


class TestOperators(unittest.TestCase):
    def test_all_operators(self):
        self.assertEqual(
            token_types("= + - * / % ( ) ,"),
            [EQUAL, PLUS, MINUS, STAR, SLASH, PERCENT, LPAREN, RPAREN, COMMA, EOF],
        )

    def test_parentheses_are_not_mixed_up(self):
        self.assertEqual(token_types("()"), [LPAREN, RPAREN, EOF])

    def test_illegal_character(self):
        with self.assertRaises(LexerError) as context:
            Lexer("let_it x = 5 $").get_tokens()
        self.assertIn("'$'", str(context.exception))


class TestStrings(unittest.TestCase):
    def test_simple_string(self):
        tokens = Lexer('"hello world"').get_tokens()
        self.assertEqual(tokens[0].type, STRING)
        self.assertEqual(tokens[0].value, "hello world")

    def test_empty_string(self):
        self.assertEqual(token_values('""'), ["", None])

    def test_escape_sequences(self):
        tokens = Lexer(r'"a\nb\tc\"d\\e"').get_tokens()
        self.assertEqual(tokens[0].value, 'a\nb\tc"d\\e')

    def test_unknown_escape_is_an_error(self):
        with self.assertRaises(LexerError):
            Lexer(r'"bad \q"').get_tokens()

    def test_unterminated_string_is_an_error(self):
        with self.assertRaises(LexerError):
            Lexer('"no end').get_tokens()

    def test_string_cannot_span_lines(self):
        with self.assertRaises(LexerError):
            Lexer('"line one\nline two"').get_tokens()


class TestLinesAndComments(unittest.TestCase):
    def test_newline_and_semicolon_end_statements(self):
        self.assertEqual(
            token_types("1\n2;3"),
            [NUMBER, NEWLINE, NUMBER, NEWLINE, NUMBER, EOF],
        )

    def test_comment_is_skipped(self):
        self.assertEqual(token_types("# just a comment"), [EOF])

    def test_comment_after_code(self):
        self.assertEqual(token_types("x # the x"), [IDENTIFIER, EOF])

    def test_line_and_column_are_tracked(self):
        tokens = Lexer("let_it x = 1\n  print(x)").get_tokens()
        print_token = tokens[5]
        self.assertEqual(print_token.type, PRINT)
        self.assertEqual((print_token.line, print_token.column), (2, 3))

    def test_error_reports_position(self):
        with self.assertRaises(LexerError) as context:
            Lexer("x = 1\ny = @").get_tokens()
        self.assertEqual((context.exception.line, context.exception.column), (2, 5))


if __name__ == "__main__":
    unittest.main()
