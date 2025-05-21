"""
Main entry point for the language to read and interpret for the code :

"""


from lexer import Lexer
from parser import Parser
from env import Environment
from interpreter import Interpreter

# source_code  = eval(input(""))
source_code  = "2 + 2"

'''
Step by Step Interpretation for the code entered and the computation of the same : 
'''


# Lexing  :  
lexer  = Lexer(source_code)
tokens  = lexer.get_tokens()

# Parsing : 
parser = Parser(tokens)
ast  = parser.parse()

# Interpreation : 
env = Environment()
interpreter  = Interpreter(env)
interpreter.interpret(ast)

