## Variable Environment File : 

class Environment:

    def __init__(self):
        self.vars  =  {} # It will be used to store the variables and values: 
    
    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        else:
            raise Exception (f"Variable : {name } not Defined ")
    
    def set(self, name  , value ):
        self.vars[name] = value
    
    
