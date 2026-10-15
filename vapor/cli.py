"""
Command line entry point.

    python -m vapor script.vp     run a Vapor script
    python -m vapor               start the interactive prompt
"""

import sys

from . import __version__
from .errors import VaporError
from .repl import start_repl
from .runner import run_file

USAGE = """usage: python -m vapor [script.vp]

  script.vp       run a Vapor script
  (no argument)   start the interactive prompt
  -h, --help      show this help
  -v, --version   show the Vapor version"""


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv

    if not argv:
        start_repl()
        return 0
    if argv[0] in ("-h", "--help"):
        print(USAGE)
        return 0
    if argv[0] in ("-v", "--version"):
        print(f"vapor {__version__}")
        return 0
    if len(argv) > 1:
        print(USAGE, file=sys.stderr)
        return 2

    try:
        run_file(argv[0])
    except VaporError as error:
        print(error, file=sys.stderr)
        return 1
    return 0
