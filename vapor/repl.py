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


def start_repl(input_fn=input, output=None):
    output = output or sys.stdout
    print(f"Vapor {__version__} - type 'exit' to quit", file=output)
    interpreter = Interpreter(Environment(), output)

    while True:
        try:
            line = input_fn(PROMPT)
        except (EOFError, KeyboardInterrupt):
            print(file=output)
            break

        if line.strip() in ("exit", "quit"):
            break
        if not line.strip():
            continue

        try:
            program = parse_source(line)
            result = interpreter.interpret(program)
            if program.statements and isinstance(program.statements[-1], ExprStatement):
                print(format_value(result), file=output)
        except VaporError as error:
            print(error, file=output)
