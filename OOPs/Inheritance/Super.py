'''
Super()

    -In Python, the super() function is used to refer to the parent class or superclass. 
    -It allows you to call methods defined in the superclass from the subclass, enabling you to extend and customize the functionality inherited from the parent class.


Syntax: 
    super()

Return : Return a proxy object which represents the parent’s class.

What is super() in Python?
    super() in Python is a built-in function that returns a proxy object (temporary object of the superclass) that allows you to access methods of a base class from a derived class. 
    -This is particularly useful in multiple inheritance, as it allows you to avoid explicitly naming the base class.

Why Do I Need super() in Python?
    Using super() helps to avoid explicitly referring to the base classes by name and ensures that the correct methods are called in the presence of multiple inheritance. 
    -It is useful for accessing overridden methods, avoiding the duplication of code, and providing a hook into cooperative multiple inheritance.

What is super().__init__()?
    super().__init__() is used to call the __init__() method of the superclass in a derived class. 
    -This is necessary when you want to ensure that the initialization code in the base class is executed before executing any in the derived class.
'''


class ParentClass:
    
    def __init__(self,name,email,id):
        self.name=name
        self.email=email
        self.id=id
        
    def get_info(self):
        print(f"ID:{self.id}\nName:{self.name}Email:\n{self.email}")
        
        
class ChildClass(ParentClass):
    def __init__(self,name,email,id,phone):
        self.phone=phone
        super().__init__(name,email,id)
        
    def get_child_info(self):
        self.get_info()
        print(f"Phone:{self.phone}")
        
        
child=ChildClass("Abhi","abhi12@gmail.com",3,"8957889130")
child.get_child_info()