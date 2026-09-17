"""
The interpreter for Vapor.

It walks the abstract syntax tree built by the parser and runs each node.
Values in Vapor are numbers (int or float) and strings.
"""

import sys

from .environment import Environment
from .errors import VaporRuntimeError


def is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def type_name(value):
    return "number" if is_number(value) else "string"


def to_text(value):
    """How a value looks when printed with print()."""
    return value if isinstance(value, str) else str(value)
