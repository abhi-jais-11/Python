'''
WHAT IS METHOD :
        -when a function is associated with an onject the it's known as the method. 
        -there are 3 type of methed in the python class.
        
        1.instance method 
        2.class method 
        3.static method 

'''

'''
1.Instance Method 
    -Instance methods are the most common type of methods in Python classes.
   -They are associated with instances of a class and operate on the instance's data. 
    -When defining an instance method, the method's first parameter is typically named self,
    -which refers to the instance calling the method. 
    -This allows the method to access and manipulate the instance's attributes.

Syntax Instance Method

    class MyClass:
        def instance_method(self, arg1, arg2, ...):
             # Instance method logic here
            pass
'''

#simple instance method 

class Instance :
    
    def instance_method(self):
        print("This is Instance Method.")
        print('------------------------------')    



instance=Instance()
#callin the instance method 
instance.instance_method()
# Instance.instance_method() TypeError: Instance.instance_method() missing 1 required positional argument: 'self'



'''
2.Class Method in Python
    -Class methods are associated with the class rather than instances. 
    -They are defined using the @classmethod decorator and take the class itself as the first parameter, usually named cls. 
    -Class methods are useful for tasks that involve the class rather than the instance, such as creating class-specific behaviors or modifying class-level attributes.

Syntax Python Class Method
    class ClassMethod:
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
fun: function that needs to be converted into a class method
returns: a class method for function.



'''

#simple class method 
class Class:
    @classmethod
    def class_method(cls):
        print("Class Method ! ")
        print('----------------------')
        
class_m=Class()
# class_m.class_method()
Class.class_method()



'''
3.Static Method in Python
    -Static methods, as the name suggests, are not bound to either the class or its instances.
    -They are defined using the @staticmethod decorator and do not take a reference to the instance or the class as their first parameter.
    -Static methods are essentially regular functions within the class namespace and are useful for tasks that do not depend on instance-specific or class-specific data.
Syntax:
class StaticMethod:
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
'''

#simple static method 


class Static:
    @staticmethod
    def static_method():
        print("Static Method !")
        

static=Static()
# Static.static_method()
static.static_method()