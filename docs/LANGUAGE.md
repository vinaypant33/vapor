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
