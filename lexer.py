from tokens import *


class Lexer():

    def __init__(self , text):
        self.text  = text
        self.pos  = 0
        if self.text:
            self.current_char = self.text[self.pos] 
        else:
            None
        
    
    # To move by one character : Each time this function has to run to make sure everything is in control : 
    def advance(self):
        self.pos+=1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    

    # Function to skip the whilespaces from the text string : 
    def skip_whitespaces(self):
        while self.current_char and self.current_char.isspace():
            self.advance()
    

    # For numbers we have to read them in full  : Means single number till there is a space : 
    def number(self):
        result  = ""
        while self.current_char and self.current_char.isdigit():
            result+=self.current_char
            self.advance()
        return Token(NUMBER , int(result))


    # To Read an identifier we have defined in the tokens : 
    def identifier(self):
        result  = ""
        while self.current_char and (self.current_char.isalum() or self.current_char == "_"):
            result+=self.current_char
            self.advance()
        if result == "let_it":
            return Token(LET_IT)
        elif result == "print":
            return Token(PRINT)
    
    def get_tokens(self):
        tokens  = []
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespaces()
            elif self.current_char.isalpha():
                tokens.append(self.identifier())
            elif self.current_char.isdigit():
                tokens.append(self.number())
            elif self.current_char == "=":
                tokens.append(Token(EQUAL))
                self.advance()
            elif self.current_char == "+":
                tokens.append(Token(PLUS))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(LPAREN))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(RPAREN))
                self.advance()
            else:
                raise Exception(f"Illegal Character : {self.current_char}")
        
        tokens.append(Token(EOF))
        return tokens 

            