"""
Nodes of the abstract syntax tree (AST).

The parser builds a tree out of these nodes; the interpreter walks the tree
to run the program. Every node remembers the line and column it came from.
"""


class Node:
    def __init__(self, line=None, column=None):
        self.line = line
        self.column = column
