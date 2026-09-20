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


def format_value(value):
    """How a value looks in the REPL: strings keep their quotes."""
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
        return f'"{escaped}"'
    return str(value)


class Interpreter:
    """Runs a Program node."""

    def __init__(self, env=None, output=None):
        self.env = env if env is not None else Environment()
        self.output = output

    def interpret(self, program):
        """Run every statement. Returns the value of the last statement."""
        result = None
        for statement in program.statements:
            result = self.eval(statement)
        return result

    def eval(self, node):
        method = getattr(self, f"eval_{type(node).__name__}", None)
        if method is None:
            raise VaporRuntimeError(
                f"Don't know how to run {type(node).__name__}", node.line, node.column
            )
        return method(node)

    def error(self, message, node):
        raise VaporRuntimeError(message, node.line, node.column)

    # ---- Statements ----

    def eval_Program(self, node):
        return self.interpret(node)

    def eval_VarDecl(self, node):
        value = self.eval(node.expression)
        self.env.declare(node.name, value, node.line, node.column)
        return None

    def eval_Assign(self, node):
        value = self.eval(node.expression)
        self.env.assign(node.name, value, node.line, node.column)
        return None

    def eval_Print(self, node):
        values = [to_text(self.eval(expression)) for expression in node.expressions]
        print(" ".join(values), file=self.output or sys.stdout)
        return None

    def eval_ExprStatement(self, node):
        return self.eval(node.expression)

    # ---- Expressions ----

    def eval_Number(self, node):
        return node.value

    def eval_String(self, node):
        return node.value

    def eval_Var(self, node):
        return self.env.get(node.name, node.line, node.column)
