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

    def string(self):
        """Read a string in double quotes, handling escape sequences."""
        line, column = self.line, self.column
        self.advance()  # skip the opening quote
        chars = []
        while True:
            if self.current_char is None or self.current_char == "\n":
                raise LexerError("String is missing its closing '\"'", line, column)
            if self.current_char == '"':
                self.advance()  # skip the closing quote
                break
            if self.current_char == "\\":
                escape_line, escape_column = self.line, self.column
                self.advance()
                if self.current_char not in ESCAPES:
                    shown = self.current_char if self.current_char is not None else ""
                    raise LexerError(
                        f"Unknown escape sequence '\\{shown}'",
                        escape_line,
                        escape_column,
                    )
                chars.append(ESCAPES[self.current_char])
                self.advance()
                continue
            chars.append(self.current_char)
            self.advance()
        return Token(STRING, "".join(chars), line, column)
