"""
The variable system for Vapor.

Variables are created with `let_it name = value` and changed with
`name = value`. The Environment stores every variable and its current value.
"""

from .errors import VaporRuntimeError


class Environment:
    """Stores the variables of a running Vapor program."""

    def __init__(self):
        self.vars = {}
