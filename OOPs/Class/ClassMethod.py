'''
Class Method :
Key Points:
    -@classmethod Decorator: Marks the method as a class method.
    -cls Parameter: Refers to the class itself, not the instance.
    -Access to Class Attributes: Class methods can access and modify class-level attributes.
    -Calling on Class or Instance: Class methods can be called on the class or an instance of the class.
    
Common Use Cases:
    -Factory methods to create instances of the class.
    -Methods that need to operate on class-level data rather than instance-specific data.
    -Alternative constructors (e.g., parsing data to create an instance).
'''

#class method 


class ClassMethod:
    
    #static varible
    name="Class Varible!"
    
    
    @classmethod 
    def change_class_variable(cls,name):
        cls.name=name
    
    
    @classmethod
    def get_name(cls):
        print(cls.name)
    
    

class_method_obj=ClassMethod()
print("------- Before Change -----------")
class_method_obj.get_name()
print("------- After Change ------------")
class_method_obj.change_class_variable("This is Change Class Varible :")
class_method_obj.get_name()
    