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
