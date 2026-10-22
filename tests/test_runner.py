import io
import tempfile
import unittest
from pathlib import Path

from vapor.errors import VaporError
from vapor.runner import run_file

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
