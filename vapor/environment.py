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

    def assign(self, name, value, line=None, column=None):
        """Change an existing variable. It must have been created first."""
        if name not in self.vars:
            raise VaporRuntimeError(
                f"Variable '{name}' is not defined. "
                f"Use 'let_it {name} = ...' to create it.",
                line,
                column,
            )
        self.vars[name] = value

    def get(self, name, line=None, column=None):
        """Read the value of a variable."""
        if name not in self.vars:
            raise VaporRuntimeError(f"Variable '{name}' is not defined", line, column)
        return self.vars[name]

    def __contains__(self, name):
        return name in self.vars
