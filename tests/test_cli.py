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

    def test_too_many_arguments(self):
        code, _, err = run_cli("a.vp", "b.vp")
        self.assertEqual(code, 2)
        self.assertIn("usage", err)


class TestRepl(unittest.TestCase):
    def run_repl(self, lines):
        inputs = iter(lines)

        def fake_input(prompt):
            try:
                return next(inputs)
            except StopIteration:
                raise EOFError

        output = io.StringIO()
        start_repl(input_fn=fake_input, output=output)
        return output.getvalue()

    def test_expression_value_is_shown(self):
        out = self.run_repl(["2 + 3"])
        self.assertIn("\n5\n", out)

    def test_variables_are_kept_between_lines(self):
        out = self.run_repl(["let_it x = 4", "x * 10"])
        self.assertIn("40", out)

    def test_strings_are_shown_with_quotes(self):
        out = self.run_repl(['"hi"'])
        self.assertIn('"hi"', out)

    def test_errors_do_not_stop_the_repl(self):
        out = self.run_repl(["print(nope)", "1 + 1"])
        self.assertIn("not defined", out)
        self.assertIn("\n2\n", out)

    def test_exit(self):
        out = self.run_repl(["exit", "print(99)"])
        self.assertNotIn("99", out)


if __name__ == "__main__":
    unittest.main()
