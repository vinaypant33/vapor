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
