"""
Vapor - a small, basic scripting language written in Python.

Vapor scripts use the .vp extension. See README.md for the language guide.
"""

__version__ = "1.0.0"

from .errors import LexerError, ParseError, VaporError, VaporRuntimeError  # noqa: E402
from .runner import run_file, run_source  # noqa: E402

__all__ = [
    "LexerError",
    "ParseError",
    "VaporError",
    "VaporRuntimeError",
    "run_file",
    "run_source",
]
