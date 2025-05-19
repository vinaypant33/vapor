# This file would conver the tokens in the ast  : 


from tokens import *
from ast_nodes import * 






class Parser():

    def __init__(self , tokens):
        self.tokens = tokens
        self.pos  = 0
        self.current_token  = self.tokens[self.pos]
    
    
    def advance(self):
        self.pos  +=1 
        if self.pos <  len(self.tokens):
            self.current_token = self.tokens[self.pos]
    

    def eat(self , token_type):
        if self.current_token.type  == token_type:
            self.advance()
        else:
            raise Exception(f"Expected {token_type} , got {self.current_token.type}")
    
    def parse(self):
        statements  = []
        while self.current_token.type != EOF:
            if self.current_token.type == LET_IT:
                statements.append(self.var_dec())
            elif self.current_token.type == PRINT:
                statements.append(self.print_stmt())
            else:
                raise Exception (f"Unexpected Token {self.current_token}")
    
    def var_dec(self):
        self.eat(LET_IT)
        var_name  = self.current_token.value
        self.eat(IDENTIFIER)
        self.eat(EQUAL)
        expr  = self.expr()
        return VarDecl(var_name  ,  expr)


    def print_stmt(self):
        self.eat(PRINT)
        self.eat(LPAREN)
        expr  = self.expr()
        self.eat(RPAREN)
        return Print(expr)

    def expr(self):
        left  = self.term()
        while self.current_token.type  == PLUS: 
            op = self.current_token
            self.eat(PLUS)
            right  = self.term()
            left  = BinOp(left , op , right)
        return left
    
    def term(self):
        token  = self.current_token
        if token.type  == NUMBER:
            self.eat(NUMBER)
            return Number(token.value)
        elif token.type  == IDENTIFIER:
            self.eat(IDENTIFIER)
            return Var(token.value)
        elif token.type  == LPAREN:
            self.eat(LPAREN)
            node  = self.expr()
            self.eat(RPAREN)
            return  node
        else:
            raise Exception("Invalid Expression")
    
    


    
    

