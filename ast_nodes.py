

# This would handle the numbers for the code 
class Number():

    def __init__(self , value):
        self.value  = value

    

class Var():

    def __init__(self , name):
        self.name  = name

class BinOp(): # Class for the binomial Operation :

    def __init__(self , left  ,  op , right):
        self.left  = left  #  Expression
        self.op = op  # Token 
        self.right = right


class VerDecl():

    def __init__(self , name  ,  expression):
        self.name  = name # Variable Name
        self.expression  = expression # Expression to assign 
    
class Print():

    def __init__(self , expression ):
        self.expression  = expression
    

class Program():

    def __init__(self , statements):
        self.statements  = statements # This would be used for the list of statements : 



    