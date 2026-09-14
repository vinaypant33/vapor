import unittest

from vapor.environment import Environment
from vapor.errors import VaporRuntimeError


class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.env = Environment()
