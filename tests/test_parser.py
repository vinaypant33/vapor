import unittest

from vapor.ast_nodes import (
    Assign,
    BinOp,
    ExprStatement,
    Number,
    Print,
    String,
    UnaryOp,
    Var,
    VarDecl,
)
from vapor.errors import ParseError
from vapor.runner import parse_source


def parse_one(source):
    program = parse_source(source)
    assert len(program.statements) == 1, program.statements
    return program.statements[0]


class TestStatements(unittest.TestCase):
    def test_empty_program(self):
        self.assertEqual(parse_source("").statements, [])
