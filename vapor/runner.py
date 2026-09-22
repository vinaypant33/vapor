"""
Helpers that run Vapor code from a string or from a .vp file.
"""

from pathlib import Path

from .errors import VaporError
from .interpreter import Interpreter
from .lexer import Lexer
from .parser import Parser

FILE_EXTENSION = ".vp"


def parse_source(source):
    """Lex and parse source code, returning the Program node."""
    tokens = Lexer(source).get_tokens()
    return Parser(tokens).parse()
