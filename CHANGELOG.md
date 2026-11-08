# Changelog

## 1.0.0

- Documentation: README and the full language guide in docs/LANGUAGE.md
- 15 example scripts in examples/
- pyproject.toml so Vapor can be installed with `pip install .`, giving a `vapor` command

## 0.5.0

- Command line: `python main.py script.vp`, `python -m vapor`, `--help`, `--version`
- Interactive prompt (REPL) that keeps variables between lines
- Only files ending in `.vp` are run

## 0.4.0

- Variable system: `let_it` creates a variable, `name = value` changes it
- Clear errors for undefined variables and variables defined twice
- `print` accepts any number of values

## 0.3.0

- New recursive-descent parser with operator precedence
- `* / %`, unary minus and parentheses
- Strings and joining text with `+`
- Errors show the line and column

## 0.2.0

- Rewritten lexer that tracks line and column
- Decimal numbers, strings with escape sequences, comments and `;`

## 0.1.0

- First working version: `let_it`, `print`, `+` and `-`
- Fixed bugs in the original lexer, parser and interpreter
