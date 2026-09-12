"""
The parser for Vapor.

It reads the list of tokens from the lexer and builds an abstract syntax tree.
The grammar, from the top down:

    program    : statement (NEWLINE statement)* EOF
    statement  : 'let_it' IDENTIFIER '=' expr
               | IDENTIFIER '=' expr
               | 'print' '(' [expr (',' expr)*] ')'
               | expr
    expr       : term (('+' | '-') term)*
    term       : factor (('*' | '/' | '%') factor)*
    factor     : ('+' | '-') factor | primary
    primary    : NUMBER | STRING | IDENTIFIER | '(' expr ')'

Splitting expr / term / factor gives '*' and '/' a higher precedence than
'+' and '-', so 2 + 3 * 4 is 14, not 20.
"""

from .ast_nodes import (
    Assign,
    BinOp,
    ExprStatement,
    Number,
    Print,
    Program,
    String,
    UnaryOp,
    Var,
    VarDecl,
)
from .errors import ParseError
from .tokens import (
    COMMA,
    EOF,
    EQUAL,
    IDENTIFIER,
    LET_IT,
    LPAREN,
    MINUS,
    NEWLINE,
    NUMBER,
    PERCENT,
    PLUS,
    PRINT,
    RPAREN,
    SLASH,
    STAR,
    STRING,
    TOKEN_DESCRIPTIONS,
)

OPERATOR_SYMBOLS = {
    PLUS: "+",
    MINUS: "-",
    STAR: "*",
    SLASH: "/",
    PERCENT: "%",
}


class Parser:
    """Turns a list of tokens into a Program node."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    @property
    def current_token(self):
        return self.tokens[self.pos]

    def peek(self, offset=1):
        """Look at a token ahead without moving."""
        index = min(self.pos + offset, len(self.tokens) - 1)
        return self.tokens[index]

    def advance(self):
        token = self.current_token
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return token

    def error(self, message, token=None):
        token = token or self.current_token
        raise ParseError(message, token.line, token.column)

    def eat(self, token_type):
        """Consume a token of the expected type, or raise a syntax error."""
        if self.current_token.type != token_type:
            expected = TOKEN_DESCRIPTIONS.get(token_type, token_type)
            self.error(f"Expected {expected} but found {self.current_token.describe()}")
        return self.advance()

    def skip_newlines(self):
        while self.current_token.type == NEWLINE:
            self.advance()

    # ---- Statements ----

    def parse(self):
        statements = []
        self.skip_newlines()
        while self.current_token.type != EOF:
            statements.append(self.statement())
            if self.current_token.type not in (NEWLINE, EOF):
                self.error(
                    "Expected a new line or ';' after the statement but found "
                    f"{self.current_token.describe()}"
                )
            self.skip_newlines()
        return Program(statements)

    def statement(self):
        token = self.current_token
        if token.type == LET_IT:
            return self.var_decl()
        if token.type == PRINT:
            return self.print_stmt()
        if token.type == IDENTIFIER and self.peek().type == EQUAL:
            return self.assignment()
        expression = self.expr()
        return ExprStatement(expression, token.line, token.column)

    def var_decl(self):
        start = self.eat(LET_IT)
        name_token = self.eat(IDENTIFIER)
        self.eat(EQUAL)
        expression = self.expr()
        return VarDecl(name_token.value, expression, start.line, start.column)

    def assignment(self):
        name_token = self.eat(IDENTIFIER)
        self.eat(EQUAL)
        expression = self.expr()
        return Assign(name_token.value, expression, name_token.line, name_token.column)

    def print_stmt(self):
        start = self.eat(PRINT)
        self.eat(LPAREN)
        expressions = []
        if self.current_token.type != RPAREN:
            expressions.append(self.expr())
            while self.current_token.type == COMMA:
                self.eat(COMMA)
                expressions.append(self.expr())
        self.eat(RPAREN)
        return Print(expressions, start.line, start.column)

    # ---- Expressions ----

    def expr(self):
        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            op = self.advance()
            right = self.term()
            node = BinOp(node, OPERATOR_SYMBOLS[op.type], right, op.line, op.column)
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in (STAR, SLASH, PERCENT):
            op = self.advance()
            right = self.factor()
            node = BinOp(node, OPERATOR_SYMBOLS[op.type], right, op.line, op.column)
        return node

    def factor(self):
        token = self.current_token
        if token.type in (PLUS, MINUS):
            self.advance()
            operand = self.factor()
            return UnaryOp(OPERATOR_SYMBOLS[token.type], operand, token.line, token.column)
        return self.primary()
