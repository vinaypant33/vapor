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

    def declare(self, name, value, line=None, column=None):
        """Create a new variable (let_it). It must not exist yet."""
        if name in self.vars:
            raise VaporRuntimeError(
                f"Variable '{name}' is already defined. "
                f"Use '{name} = ...' to change its value.",
                line,
                column,
            )
        self.vars[name] = value
