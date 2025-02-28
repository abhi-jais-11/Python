'''
__init__():
    The __init__() method in Python is a special method used to initialize objects of a class. 
    It is automatically called when an instance of the class is created. Here's a structured explanation:

Key Points About __init__():
    Purpose:
        Initializes the object's attributes.
        Sets up the initial state of the object.

Syntax:
    class MyClass:
        def __init__(self, param1, param2):
            self.param1 = param1  # Instance variable
            self.param2 = param2

self refers to the instance being created (mandatory first parameter).
Additional parameters define values needed to initialize the object.
Invocation:
    Called automatically when an object is instantiated:
    obj = MyClass(arg1, arg2)  # Triggers __init__

'''

#simple example 

class Constructor:
    
    def __init__(self):
        print("Contructor Called ! But It's Not Actual Contructor")
        print('---------------------------------------------------')
    
con=Constructor()

        
'''
type of __init__
1.default
2.parameterize
3.non-parameterize
4.No Return Value:
        Must return None. Returning any other value raises an error.
'''



#1. Default if we are not creating a __init__ in python the PVM autometically create a default __init__ method.

class Default:
    print("Default INIT Method !")
    print('---------------------------------------------------')
     
default=Default()


#2.Parametrize 

class Parameterize:
    
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print(f"Name:{self.name}\nAge:{self.age}")
        print('---------------------------------------------------')
        return None
        # return name TypeError: __init__() should return None, not 'str'
        
        
        


parameterize=Parameterize("Jack Son ",22)


#3.non-parametrize

class NonParametrize:
    
    def __init__(self):
        print("Non Parametrize ")
        print('---------------------------------------------------')
        

nonp=NonParametrize()
        
    
    
'''
If a single class has more then one __init__ method  with different parameter last one will be execute with the parameter.
Bcz of the python does not support method overloading.

To solve this problem We can Use default parameter or if else statement.
But it is highly recomnded to use only one __init__ method in a single class.

'''

class Double_Init:
    
    def __init__(self):
        print("First Without Argumemt !")
    
    def __init__(self):
        print("Last Without Argumemt !")
        print('---------------------------------------------------')
    
    

buble=Double_Init()

# 

class Triple:
    def __init__(self):
        print("First Without Argumemt !")
    
    def __init__(self):
        print("Second  Without Argumemt !")
      
        
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"Name:{self.name}\nAge:{self.age}")
        print('---------------------------------------------------')
    

# triple=Triple() TypeError: Triple.__init__() missing 2 required positional arguments: 'name' and 'age'
triple=Triple("Jack Hunt",22)


# solving the problem of type error
class Triple:
    def __init__(self):
        print("First Without Argumemt !")
    
    def __init__(self):
        print("Second  Without Argumemt !")
      
        
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
        if name is not None and age is not None: 
            print(f"Name:{self.name}\nAge:{self.age}")
        else:
            print("Name And Age Is Not Provided !")
        
        print('---------------------------------------------------')
    

triple=Triple()
triple=Triple("Jack Hunt",22)



# we can call __init__method explicitly using object outside of the class.

class Explicit_Init:
    
    def __init__(self,str):
        self.str=str
        print(str)
    
    def Self(self):
        self.__init__("Using Self Called !")
        

exp=Explicit_Init("Autometically Called !")
exp.__init__("Using Object Called !")       
exp.Self()
print('-------------------------------------')