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


def run_source(source, env=None, output=None):
    """Run Vapor source code. Returns the value of the last statement."""
    program = parse_source(source)
    return Interpreter(env, output).interpret(program)


def run_file(path, output=None):
    """Run a Vapor script. The file must have the .vp extension."""
    path = Path(path)
    if path.suffix != FILE_EXTENSION:
        raise VaporError(
            f"Vapor scripts must end in '{FILE_EXTENSION}', got '{path.name}'"
        )
    if not path.is_file():
        raise VaporError(f"File not found: {path}")
    source = path.read_text(encoding="utf-8")
    return run_source(source, output=output)
