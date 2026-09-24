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

    def test_blank_lines_only(self):
        self.assertEqual(parse_source("\n\n;\n").statements, [])

    def test_variable_declaration(self):
        node = parse_one("let_it x = 5")
        self.assertIsInstance(node, VarDecl)
        self.assertEqual(node.name, "x")
        self.assertIsInstance(node.expression, Number)
        self.assertEqual(node.expression.value, 5)

    def test_assignment(self):
        node = parse_one("x = 7")
        self.assertIsInstance(node, Assign)
        self.assertEqual(node.name, "x")

    def test_print_with_one_value(self):
        node = parse_one('print("hi")')
        self.assertIsInstance(node, Print)
        self.assertEqual(len(node.expressions), 1)
        self.assertIsInstance(node.expressions[0], String)

    def test_print_with_many_values(self):
        node = parse_one("print(1, x, 3)")
        self.assertEqual(len(node.expressions), 3)
        self.assertIsInstance(node.expressions[1], Var)
