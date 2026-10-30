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

## The language in one minute

```
# Comments start with #

let_it price = 250          # create a variable
let_it quantity = 3
let_it total = price * quantity

total = total - 50          # change an existing variable

print("Total:", total)      # Total: 700
print("Each: " + total / quantity)

let_it a = 1; let_it b = 2  # ; puts two statements on one line
print(a + b * 10)           # 21  (* before +)
print((a + b) * 10)         # 30
```

The full guide is in [docs/LANGUAGE.md](docs/LANGUAGE.md).

## Error messages

Vapor tells you what went wrong and where:

```
SyntaxError (line 2, column 10): Expected '=' but found number 5
RuntimeError (line 4, column 7): Variable 'totl' is not defined
LexerError (line 1, column 12): Illegal character '$'
```

## Project layout

```
vapor/
├── main.py              run a script or start the prompt
├── vapor/
│   ├── tokens.py        token types
│   ├── lexer.py         source text  -> tokens
│   ├── ast_nodes.py     syntax tree nodes
│   ├── parser.py        tokens       -> syntax tree
│   ├── environment.py   the variable system
│   ├── interpreter.py   syntax tree  -> results
│   ├── errors.py        LexerError, SyntaxError, RuntimeError
│   ├── runner.py        run a string or a .vp file
│   ├── repl.py          the interactive prompt
│   └── cli.py           command line options
├── examples/            sample .vp scripts
├── tests/               unit tests
└── docs/LANGUAGE.md     the language guide
```

## How it works

```
 source code ──► Lexer ──► tokens ──► Parser ──► syntax tree ──► Interpreter ──► output
 let_it x = 2+3           LET_IT          VarDecl(x)            x = 5
                          IDENTIFIER:x      BinOp(+)
                          EQUAL               2   3
                          NUMBER:2 ...
```

1. **Lexer** (`lexer.py`) reads the text one character at a time and groups
   characters into tokens, tracking the line and column of each one.
2. **Parser** (`parser.py`) is a recursive-descent parser. It checks the
   tokens follow the grammar and builds a tree of nodes. Operator precedence
   comes from the grammar: `expr` handles `+ -`, `term` handles `* / %`.
3. **Interpreter** (`interpreter.py`) walks the tree. Variables are stored in
   an `Environment` (`environment.py`).
