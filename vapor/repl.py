"""
The interactive Vapor prompt (REPL: Read, Evaluate, Print, Loop).

Type a statement and press Enter. Variables are kept between lines, and the
value of an expression is shown straight away:

    vapor> let_it x = 5
    vapor> x * 2
    10
"""

import sys

from . import __version__
from .ast_nodes import ExprStatement
from .environment import Environment
from .errors import VaporError
from .interpreter import Interpreter, format_value
from .runner import parse_source

PROMPT = "vapor> "
