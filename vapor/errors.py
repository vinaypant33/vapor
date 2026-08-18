"""
Errors raised while running Vapor code.

Every error knows the line and column it happened at (when available), so the
message shown to the user looks like:

    SyntaxError (line 3, column 7): Expected '=' but found number 5
"""


class VaporError(Exception):
    """Base class for every error the Vapor language can raise."""

    kind = "Error"

    def __init__(self, message, line=None, column=None):
        super().__init__(message)
        self.message = message
        self.line = line
        self.column = column
