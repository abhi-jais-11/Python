'''
Inner Class in Python.
    -A class defined in another class is known as an inner class or nested class.
    - If an object is created using child class means inner class then the object can also be used by parent class or root class.
    - A parent class can have one or more inner classes but generally inner classes are avoided.
    - We can make our code even more object-oriented by using an inner class. A single object of the class can hold multiple sub-objects. We can use multiple sub-objects to give a good structure to our program.
'''

#simple example of the innerclass

class OuterClass:
    def __init__(self):
        print("Outer Class Constructor :")
        
        #inside the class using self
        self.inner_obj=self.InnerClass()
        
    def outer_method(self):
        print("Outer Class Method:")
        
    class InnerClass:
        def __init__(self):
            print("Inner  Class Constructor :")
        
        def outer_method(self):
            print("Inner Class Method:")
        

outer_object=OuterClass()
# inner_object=outer_object.InnerClass() outside of the class using object


'''
Why inner class?
    -Hiding the code is another good feature of the inner class From outer world.
    - By using the inner class, we can easily understand the classes because the classes are closely related. We do not need to search for classes in the whole code, they all are almost together. 

Types of inner classes are as follows: 
    Multiple inner class
    Multilevel inner class
'''

'''
Multiple inner class
    The class contains one or more inner classes known as multiple inner classes.
    We can have multiple inner class in a class, it is easy to implement multiple inner classes. 

'''

print("_-------------------Multiple Inner Class-------------------------_")
class Mobile:
    
    def __init__(self):
        print("All Mobile Brands:")
        self.Apple()
        self.Google()
        self.Samsung()
        
    
    class Samsung:
        def __init__(self):
            print("Samsung Mobile Brands:")
    
    class Google:
        def __init__(self):
            print("Google Mobile Brands:")
    
    class Apple:
        def __init__(self):
            print("Apple Mobile Brands:")
        
    
mobile_object=Mobile()

'''
Multilevel inner class
    -The class contains an inner class and that inner class again contains another inner class.
    -This hierarchy is known as the multilevel inner class.
'''


print("_-------------------Multilevel Inner Class-------------------------_")
class GrandFather:
    
    def __init__(self):
       print("GrandFather Class:")
       self.Father()
    
    
    class Father:

        def __init__(self):
           print("Father Class:")
           self.Child()
           
        
        class Child:

            def __init__(self):
               print("Child Class:")
    

grand_father_object=GrandFather()