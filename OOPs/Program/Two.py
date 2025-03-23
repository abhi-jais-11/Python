class Calculator:
    '''
    Simple calculator class.
    
    '''
    def __init__(self, *args, **kwargs):
        pass
    
    @staticmethod
    def add(*args):
        print(f"Sum of Nums is:{sum(args)}")
    
    @staticmethod
    def sub(a,b):
        print(f"Sub of Nums is:{a-b}")


#object 

calc=Calculator()
calc.add(10,20)
calc.sub(20,10)