'''
1.Abstract Method:
    - Abstract Means  Not Complete.
    - only declaration but not proper implementation.
    - @abstractmethod decorator is use to declare the abstract method .
    - This method  is availabe in abc module  we need to import like this.
    - from abc import ABC, abstractmethod    --> ABC is a class   use both for abstraction else not abstraction in python.

'''

#symple example 

from abc import *
class Fruit(ABC):
    @abstractmethod
    def taste(self): #abtract method 
        pass




'''
2.Abstract Class :
    - Prtially implemented class known as the abstract class.
    - Python abc module provide ABC => Abstract Base Class we need to Inherit.
    - It can contains both abstract or normal method.
    - Child classes are responsible to provide proper implementation of parent class abstract class. 
    - If a class extending ABC class and contains atleast one abstract method , then object creation is not possible.    
'''

#simple abstract class
class Fruit(ABC): #abstract class
    @abstractmethod
    def taste(self): #abtract method 
        pass




#syntactically  correct but not use in abstract 
#this is partially abstract
class Demo:
    @abstractmethod
    def demo(self):
        print("Hello from Abstract")
        pass

# d=Demo()
# d.demo()

class Demo(ABC):
    def demo(self):
        print("Hello from Abstract")
        pass

# d=Demo()
# d.demo()


'''
 If a class extending ABC class and contains atleast one abstract method ,
 Then object creation is not possible. 
 We need to implement the logic inside the child class .

'''

#example
class Demo(ABC): #fullyabstract class force to follow the rule .that implement the login in child class
    @abstractmethod
    def demo(self):
        pass

# d=Demo() #TypeError: Can't instantiate abstract class Demo without an implementation for abstract method 'demo'
# d.demo()


'''
1.Not Valid 

class Fruit(ABC): #abstract class
    @abstractmethod
    def taste(self): #abtract method 
        pass

class Mango(Fruit):pass 
    #child must be override the method of parent class then it'll valid.[not use pass]

obj=Mango()
'''
#solving the problem

class Parent(ABC):
    @abstractmethod
    def info(self):
        pass

class Child(Parent):
    def __init__(self, *args, **kwargs):
        self.data=kwargs
        
    def info(self):
        for key,value in self.data.items():
            print(f"{key.capitalize()}:{value}")



#object creation
obj=Child(name="Jenna Ortega",age=23,work="Model")
obj2=Child(name="Jenna Ortega",age=23)
obj.info()
print('----------')
obj2.info()
        
        