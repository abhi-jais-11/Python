class Greeter:
    '''
    Simple Class Greeting with Name.
    
    '''
    def __init__(self, *args, **kwargs):
        pass
    
    def greet(self,name):
        print(f"Hello Welcome {name} !")
    

#object creation
greet_name=Greeter()
greet_name.greet("Jack")
