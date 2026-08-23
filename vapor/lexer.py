"""
The lexer (lexical analyser) for Vapor.

It reads the source code one character at a time and groups the characters
into tokens: numbers, strings, names, keywords and operators. Spaces and
comments are skipped, line breaks become NEWLINE tokens.
"""

from .errors import LexerError
from .tokens import (
    COMMA,
    EOF,
    EQUAL,
    IDENTIFIER,
    KEYWORDS,
    LPAREN,
    MINUS,
    NEWLINE,
    NUMBER,
    PERCENT,
    PLUS,
    RPAREN,
    SLASH,
    STAR,
    STRING,
    Token,
)

# Characters that always form a token on their own.
SINGLE_CHAR_TOKENS = {
    "=": EQUAL,
    "+": PLUS,
    "-": MINUS,
    "*": STAR,
    "/": SLASH,
    "%": PERCENT,
    "(": LPAREN,
    ")": RPAREN,
    ",": COMMA,
    ";": NEWLINE,
}

# Escape sequences allowed inside strings, e.g. "line one\nline two".
ESCAPES = {
    "n": "\n",
    "t": "\t",
    '"': '"',
    "\\": "\\",
}

WHITESPACE = " \t\r"


class Lexer:
    """Turns Vapor source code into a list of tokens."""

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.current_char = self.text[0] if self.text else None

    def advance(self):
        """Move one character forward, keeping track of line and column."""
        if self.current_char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char in WHITESPACE:
            self.advance()

    def skip_comment(self):
        """Comments start with '#' and run to the end of the line."""
        while self.current_char is not None and self.current_char != "\n":
            self.advance()

    def number(self):
        """Read a whole number (42) or a decimal number (3.14)."""
        line, column = self.line, self.column
        result = ""
        seen_dot = False
        while self.current_char is not None and (
            self.current_char.isdigit() or self.current_char == "."
        ):
            if self.current_char == ".":
                if seen_dot:
                    raise LexerError(
                        f"Number '{result}.' has more than one decimal point",
                        line,
                        column,
                    )
                seen_dot = True
            result += self.current_char
            self.advance()

        if result.endswith("."):
            raise LexerError(
                f"Number '{result}' needs a digit after the decimal point",
                line,
                column,
            )
        value = float(result) if seen_dot else int(result)
        return Token(NUMBER, value, line, column)

    def identifier(self):
        """Read a variable name or a keyword such as 'let_it'."""
        line, column = self.line, self.column
        result = ""
        while self.current_char is not None and (
            self.current_char.isalnum() or self.current_char == "_"
        ):
            result += self.current_char
            self.advance()

        if result in KEYWORDS:
            return Token(KEYWORDS[result], None, line, column)
        return Token(IDENTIFIER, result, line, column)
