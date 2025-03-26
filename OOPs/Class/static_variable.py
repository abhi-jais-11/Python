'''
Static Variables or Class Level Variable.
If the value of a variable is not changing from object to object, such types of variables are called static variables or class level variables. 
We can access static variables either by class name or by object name.
Accessing static variables with class names is highly recommended than object names.

Way to create static variable.
    1.Using class name in all method.
    2.Directly inside the class.
    3.In class method using cls.
    
'''

class StaticVariable:
    static_var="Static Variable"
    def __init__(self,name,age):
        StaticVariable.name=name
        StaticVariable.age=age
        print(f"Using ClassName in Constructor:\nName:{StaticVariable.name}\nAge:{StaticVariable.age}")
    
    def set_static_var_instance_method(self,name,age):
        StaticVariable.name=name
        StaticVariable.age=age
        print(f"Using ClassName in InstanceMethod:\nName:{StaticVariable.name}\nAge:{StaticVariable.age}")
    
    @classmethod
    def set_static_var_class_method(cls,name,age):
        StaticVariable.name=name
        StaticVariable.age=age
        #or
        cls.name=name
        cls.age=age
        print(f"Using ClassName in class methos and cls argument:\nName:{StaticVariable.name}\nAge:{StaticVariable.age}")
        print('--------------')
        print(f"\nName:{cls.name}\nAge:{cls.age}")
        
    @staticmethod
    def set_static_var_static_method(name,age):
        StaticVariable.name=name
        StaticVariable.age=age
        print(f"Using ClassName in StaticMethod:\nName:{StaticVariable.name}\nAge:{StaticVariable.age}")
    
        
    


#object creation
static_var=StaticVariable("Jack",22)
print('-----------------------')
static_var.set_static_var_instance_method("Rahul",24)
print('-----------------------')
static_var.set_static_var_class_method("Raj",25)
print('-----------------------')
static_var.set_static_var_static_method("Raju",26)
print('-----------------------')
print(f"Inside Class Directly:{static_var.static_var}")