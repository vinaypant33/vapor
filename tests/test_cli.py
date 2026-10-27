import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from vapor import __version__
from vapor.cli import main
from vapor.repl import start_repl


def run_cli(*args):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = main(list(args))
    return code, out.getvalue(), err.getvalue()


def write_script(name, text):
    path = Path(tempfile.mkdtemp()) / name
    path.write_text(text, encoding="utf-8")
    return str(path)


class TestCli(unittest.TestCase):
    def test_version(self):
        code, out, _ = run_cli("--version")
        self.assertEqual(code, 0)
        self.assertIn(__version__, out)

    def test_help(self):
        code, out, _ = run_cli("--help")
        self.assertEqual(code, 0)
        self.assertIn("usage", out)

    def test_run_script(self):
        code, out, _ = run_cli(write_script("ok.vp", 'print("from cli")'))
        self.assertEqual(code, 0)
        self.assertEqual(out, "from cli\n")

    def test_error_exit_code(self):
        code, _, err = run_cli(write_script("bad.vp", "print(missing)"))
        self.assertEqual(code, 1)
        self.assertIn("RuntimeError (line 1", err)
