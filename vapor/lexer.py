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
