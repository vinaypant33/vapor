import unittest

from vapor.environment import Environment
from vapor.errors import VaporRuntimeError


class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.env = Environment()

    def test_declare_and_get(self):
        self.env.declare("x", 10)
        self.assertEqual(self.env.get("x"), 10)

    def test_get_unknown_variable(self):
        with self.assertRaises(VaporRuntimeError):
            self.env.get("missing")

    def test_declare_twice_is_an_error(self):
        self.env.declare("x", 1)
        with self.assertRaises(VaporRuntimeError) as context:
            self.env.declare("x", 2)
        self.assertIn("already defined", str(context.exception))

    def test_assign_changes_value(self):
        self.env.declare("x", 1)
        self.env.assign("x", 2)
        self.assertEqual(self.env.get("x"), 2)

    def test_assign_unknown_variable_is_an_error(self):
        with self.assertRaises(VaporRuntimeError) as context:
            self.env.assign("y", 5)
        self.assertIn("let_it y", str(context.exception))

    def test_contains_and_names(self):
        self.env.declare("b", 1)
        self.env.declare("a", 2)
        self.assertIn("a", self.env)
        self.assertNotIn("c", self.env)
        self.assertEqual(self.env.names(), ["a", "b"])

    def test_variable_can_change_type(self):
        self.env.declare("x", 1)
        self.env.assign("x", "now text")
        self.assertEqual(self.env.get("x"), "now text")


if __name__ == "__main__":
    unittest.main()
