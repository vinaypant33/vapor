import io
import tempfile
import unittest
from pathlib import Path

from vapor.errors import VaporError
from vapor.runner import run_file

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"


class TestRunFile(unittest.TestCase):
    def write_temp(self, name, text):
        folder = Path(tempfile.mkdtemp())
        path = folder / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_runs_vp_file(self):
        path = self.write_temp("prog.vp", 'let_it x = 2\nprint("x =", x)\n')
        buffer = io.StringIO()
        run_file(path, output=buffer)
        self.assertEqual(buffer.getvalue(), "x = 2\n")
