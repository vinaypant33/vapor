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
