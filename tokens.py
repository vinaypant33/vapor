

# Enum Style for all the tokens that would be in the programming language : 
LET_IT  = "LET_IT"
PRINT = "PRINT"
IDENTIFIER = "IDENTIFIER"
EQUAL  = "EQUAL"
NUMBER  =  "NUMBER"
PLUS = "PLUS"
MINUS  = "MINUS"
LPAREN  = "LPAREN"
RPAREN  = "RPAREN"
EOF  = "EOF"


# Class to hold the value when the reader is working : 
class Token():

    def __init__(self , type_ , value  = None):
        self.type = type_
        self.value  = value

    
    def __repr__(self):
        if self.value : 
            return f'{self.type} : {self.value}'
        return f"{self.type}"

