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
