
'''
 1.Single Inheritance: A child class inherits from one parent class.

'''

class ParentClass:
    
    name="Parent Method Variable "
    
    
    def __init__(self):
        print("Parent Class Constructor !")
        
    def parent_method(self):
        
        print("Parent Method !!")
        


class ChildClass(ParentClass):
    
    def __init__(self):
        #super method is use to use the method and the property of the parent clas in child class .
        print("Child Constuctor !")

print('-----------------Using Parent Object -----------------------')
parent=ParentClass()
parent.parent_method()
print('-----------------Using Child Object -----------------------')
child=ChildClass()
child.parent_method()
print(child.name,"Using The Child Object:" )