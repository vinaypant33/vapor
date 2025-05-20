'''
Interpreter is used to interpret everything and is used as the second file for the entry 
to run the program which reads the instructions : 

'''



from ast_nodes import *


class Interpreter(): 

    def __init__(self , env):
        self.env  = env 
    
    def interpret(self, program):
        for stmt in program.statements:
            self.eval(stmt)
        
    
    def eval(self, node):
        if isinstance(node , Number):
            return node.value
        elif isinstance(node , Var):
            return self.env.get(node.name)
        elif isinstance(node ,  BinOp):
            left = self.eval(node.left)
            right  = self.eval(node.right)
            if node.op.tpe == 'PLUS':
                return left + right
        elif isinstance(node, VarDecl):
            value = self.eval(node.expr)
            self.env.set(node.name, value)
        elif isinstance(node, Print):
            value = self.eval(node.expr)
            print(value)