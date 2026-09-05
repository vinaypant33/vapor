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
