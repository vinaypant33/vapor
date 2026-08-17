"""
Token types for the Vapor language.

The lexer turns source code into a list of Token objects. Every token has a
type (one of the constants below), an optional value, and the line/column
where it starts so that error messages can point at the right place.
"""

# Keywords
LET_IT = "LET_IT"
PRINT = "PRINT"

# Names and literal values
IDENTIFIER = "IDENTIFIER"
NUMBER = "NUMBER"
STRING = "STRING"

# Operators
EQUAL = "EQUAL"
PLUS = "PLUS"
MINUS = "MINUS"
STAR = "STAR"
SLASH = "SLASH"
PERCENT = "PERCENT"

# Punctuation
LPAREN = "LPAREN"
RPAREN = "RPAREN"
COMMA = "COMMA"

# Structure
NEWLINE = "NEWLINE"  # end of a statement: a line break or ';'
EOF = "EOF"  # end of the source code

# Words that have a special meaning and cannot be used as variable names.
KEYWORDS = {
    "let_it": LET_IT,
    "print": PRINT,
}

# Human friendly names, used in error messages.
TOKEN_DESCRIPTIONS = {
    LET_IT: "'let_it'",
    PRINT: "'print'",
    IDENTIFIER: "a variable name",
    NUMBER: "a number",
    STRING: "a string",
    EQUAL: "'='",
    PLUS: "'+'",
    MINUS: "'-'",
    STAR: "'*'",
    SLASH: "'/'",
    PERCENT: "'%'",
    LPAREN: "'('",
    RPAREN: "')'",
    COMMA: "','",
    NEWLINE: "end of line",
    EOF: "end of file",
}
