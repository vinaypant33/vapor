# The Vapor language guide

This guide covers everything Vapor can do. Vapor is kept basic on purpose:
variables, numbers, strings, arithmetic and printing.

## Scripts

A Vapor script is a plain text file with the `.vp` extension. Run it with:

```
python main.py my_script.vp
```

Vapor refuses files with any other extension.

## Statements

A script is a list of statements, one per line:

```
let_it x = 1
print(x)
```

Use `;` to put more than one statement on the same line:

```
let_it x = 1; let_it y = 2; print(x + y)
```

Blank lines are ignored.

## Comments

Everything after `#` on a line is ignored:

```
# This whole line is a comment
let_it speed = 60   # km per hour
```

## Variables

Create a variable with `let_it`:

```
let_it name = "Vapor"
let_it count = 10
```

Change it later with `=` (no `let_it`):

```
count = count + 1
```

The rules:

| You write | When the variable... | Result |
|---|---|---|
| `let_it x = 1` | does not exist yet | creates `x` |
| `let_it x = 1` | already exists | error: already defined |
| `x = 2` | already exists | changes `x` |
| `x = 2` | does not exist | error: not defined, use `let_it` |
| `x` (reading it) | does not exist | error: not defined |

Variable names use letters, digits and `_`, and cannot start with a digit:
`total`, `item_2`, `_temp`. Names are case sensitive, so `Total` and
`total` are different variables. The keywords `let_it` and `print` cannot be
used as names.

A variable can hold a number, then later a string, or the other way round.

## Numbers

Whole numbers (`42`) and decimal numbers (`3.14`). A decimal number needs a
digit after the point: `5.` is an error, write `5.0`.

## Strings

Strings go in double quotes: `"hello"`. These escape sequences work inside a
string:

| Write | Get |
|---|---|
| `\n` | a new line |
| `\t` | a tab |
| `\"` | a double quote |
| `\\` | a backslash |

A string must end on the same line it starts.

## Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide | `7 / 2` | `3.5` |
| `%` | remainder | `7 % 2` | `1` |
| `-x` | negative | `-7` | `-7` |

Dividing two whole numbers gives a whole number when there is no remainder
(`10 / 2` is `5`), and a decimal when there is (`7 / 2` is `3.5`).

Dividing by zero, or `% 0`, is an error.

**Order of operations:** `*`, `/` and `%` happen before `+` and `-`.
Operators of the same level go left to right. Use parentheses to change the
order:

```
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20
print(10 - 4 - 3)    # 3
```

## Joining text

`+` joins text when either side is a string. Numbers are turned into text:

```
let_it age = 30
print("Age: " + age)        # Age: 30
print(1 + "st place")       # 1st place
```

The other operators only work on numbers: `"a" - "b"` and `"ab" * 3` are
errors.

## print

`print(...)` shows values, separated by spaces, and then starts a new line:

```
let_it x = 3
print("x is", x)    # x is 3
print()             # an empty line
```

Strings are printed without their quotes.
