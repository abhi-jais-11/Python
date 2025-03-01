'''
Method Overriding in Python

    -Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. 
    -When a method in a subclass has the same name, the same parameters or signature, and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.


'''

#method overriding

class ParentClass:
    
    def show(self):
        print("Parent Show Method :")


class ChildClass(ParentClass):
    
    def show(self):
        print("Child  Show Method :")
        
        
p=ParentClass()
c=ChildClass()
p.show()
c.show()

print("-------------------------Using Super()--------------------")

#Calling the Parent’s method within the overridden method
#Parent class methods can also be called within the overridden methods. This can generally be achieved by two ways.
#Using Classname: Parent’s class methods can be called by using the Parent classname.method inside the overridden method.

class ParentClass:
    
    def show(self):
        print("Parent Show Method :")


class ChildClass(ParentClass):
    
    def show(self):
        print("Child  Show Method :")
        
class ParentClass:
    
    def show(self):
        print("Parent Show Method :")


class ChildClass(ParentClass):
    
    def show(self):
        #calling parent method
        super().show()
        print("Child  Show Method :")
        
        
p=ParentClass()
c=ChildClass()
c.show()