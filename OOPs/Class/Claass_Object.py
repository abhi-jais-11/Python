'''
what is class ?

    -A class in Python is a user-defined template for creating objects.
    -It bundles data and functions together, making it easier to manage and use them.
    -When we create a new class, we define a new type of object. 
    -We can then create multiple instances of this object type.
    -Classes are created using class keyword.
    -Attributes are variables defined inside the class and represent the properties of the class. 
    -Attributes can be accessed using the dot . operator (e.g., MyClass.my_attribute).
    
    Syntax:
        class class_name:
            #attributes
            #methods
            

whst is object?
    -An Object is an instance of a Class.
    -t represents a specific implementation of the class and holds its own data.

State: 
    It is represented by attributes of an object.
    It also reflects the properties of an object.
Behavior: 
    It is represented by methods of an object. 
    It also reflects the response of an object with other objects.
Identity: 
    It gives a unique name to an object and enables one object to interact with other objects.


    Syntax:
        object_name=Classname()
    
'''

#simple greet class

class Greet: 
    def __init__(self):
        greet=f"Hello Welcome To the Class:" #class attribute
        print(greet)
    

#object
greet=Greet()



#simple Students class 

class Student:
    def __init__(self):
        self.name=input("Enter The Name:")
        self.age=int(input("Enter the Age of the Student:"))
        print(f"Name:{self.name}\n Age:{self.age}")
    
#object
student=Student()