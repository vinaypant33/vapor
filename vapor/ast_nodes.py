"""
Nodes of the abstract syntax tree (AST).

The parser builds a tree out of these nodes; the interpreter walks the tree
to run the program. Every node remembers the line and column it came from.
"""


class Node:
    def __init__(self, line=None, column=None):
        self.line = line
        self.column = column

    def __repr__(self):
        fields = ", ".join(
            f"{name}={value!r}"
            for name, value in vars(self).items()
            if name not in ("line", "column")
        )
        return f"{type(self).__name__}({fields})"


# ---- Expressions: things that produce a value ----


class Number(Node):
    """A number literal such as 42 or 3.14."""

    def __init__(self, value, line=None, column=None):
        super().__init__(line, column)
        self.value = value


class String(Node):
    """A string literal such as "hello"."""

    def __init__(self, value, line=None, column=None):
        super().__init__(line, column)
        self.value = value


class Var(Node):
    """Reading the value of a variable."""

    def __init__(self, name, line=None, column=None):
        super().__init__(line, column)
        self.name = name


class BinOp(Node):
    """A binary operation such as a + b. `op` is the symbol, e.g. "+"."""

    def __init__(self, left, op, right, line=None, column=None):
        super().__init__(line, column)
        self.left = left
        self.op = op
        self.right = right


class UnaryOp(Node):
    """A unary operation such as -x."""

    def __init__(self, op, operand, line=None, column=None):
        super().__init__(line, column)
        self.op = op
        self.operand = operand


# ---- Statements: things that do something ----


class VarDecl(Node):
    """let_it name = expression"""

    def __init__(self, name, expression, line=None, column=None):
        super().__init__(line, column)
        self.name = name
        self.expression = expression


class Assign(Node):
    """name = expression (the variable must already exist)"""

    def __init__(self, name, expression, line=None, column=None):
        super().__init__(line, column)
        self.name = name
        self.expression = expression


class Print(Node):
    """print(expression, expression, ...)"""

    def __init__(self, expressions, line=None, column=None):
        super().__init__(line, column)
        self.expressions = expressions
