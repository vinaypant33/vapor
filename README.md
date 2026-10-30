# Vapor

Vapor is a small, basic scripting language written in pure Python, with no
outside libraries. It was built to learn how programming languages work on
the inside: a **lexer** that reads characters, a **parser** that builds a
syntax tree, and an **interpreter** that runs it.

Vapor scripts use the **`.vp`** file extension.

```
# hello.vp
let_it name = "Vapor"
let_it year = 2025
print("Hello from " + name + "!")
print("Built in", year)
```

```
$ python main.py hello.vp
Hello from Vapor!
Built in 2025
```

## Features

- Variables: create them with `let_it`, change them with `=`
- Numbers (whole and decimal) and strings
- Arithmetic: `+ - * / %`, parentheses and negative numbers
- Joining text with `+` (`"Age: " + 30`)
- `print(...)` with any number of values
- Comments with `#`
- Statements on separate lines, or on one line with `;`
- Clear error messages with the line and column of the problem
- An interactive prompt (REPL) for trying things out

## Requirements

- Python 3.8 or newer
- Nothing else: Vapor only uses the Python standard library

## Running Vapor

Run a script:

```
python main.py examples/hello.vp
```

or, the same thing using the package directly:

```
python -m vapor examples/hello.vp
```

Start the interactive prompt by leaving out the file name:

```
$ python main.py
Vapor 1.0.0 - type 'exit' to quit
vapor> let_it x = 5
vapor> x * 2
10
vapor> print("x is", x)
x is 5
vapor> exit
```

Other options: `--help` and `--version`.

You can also install it, which gives you a `vapor` command:

```
pip install .
vapor examples/hello.vp
```
