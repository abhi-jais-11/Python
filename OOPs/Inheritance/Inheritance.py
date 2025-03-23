'''
inheritance in Python
    -Inheritance is a fundamental concept in object-oriented programming (OOP).
    -That allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class). 
    -This promotes code reuse, modularity, and a hierarchical class structure. 

Syntax for Inheritance
    class ParentClass:
         # Parent class code here
          pass

class ChildClass(ParentClass):
     # Child class code here
      pass

Types of Python Inheritance
    1.Single Inheritance: A child class inherits from one parent class.
    2.Multiple Inheritance: A child class inherits from more than one parent class.
    3.Multilevel Inheritance: A class is derived from a class which is also derived from another class.
    4.Hierarchical Inheritance: Multiple classes inherit from a single parent class.
    5.Hybrid Inheritance: A combination of more than one type of inheritance.
    
'''

#example.


class ParentClass:
    
    def __init__(self):
        print("Parent Constructor !")
        



class ChildClass(ParentClass):
    def __init__(self):
        print("Child  Contructor ")
        


parent=ParentClass()
child=ChildClass()

    
'''
Explanation of Python Inheritance Syntax
Parent Class:
    This is the base class from which other classes inherit.
    It contains attributes and methods that the child class can reuse.
Child Class:
    This is the derived class that inherits from the parent class.
    The syntax for inheritance is class ChildClass(ParentClass).
    The child class automatically gets all attributes and methods of the parent class unless overridden.

'''