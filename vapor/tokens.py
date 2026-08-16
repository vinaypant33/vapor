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
