'''
2.Multiple Inheritance: A child class inherits from more than one parent class.

'''

class ParentOne:
    
    def __init__(self):
        print("Parent One !")
    def parent_one_method(self):
        print("Parent One Method!")
        

class ParentTwo:
    def __init__(self):
        print("Parent Two !")
    def parent_two_method(self):
        print("Parent Two Method!")



class Child (ParentTwo,ParentOne):
    def __init__(self):
        ParentOne.__init__(self)
        ParentTwo.__init__(self)
        print("Child Class")
        self.parent_two_method()
        self.parent_one_method()
        
  
print("------------------Child Access The Parent ------------------------")
c=Child()



