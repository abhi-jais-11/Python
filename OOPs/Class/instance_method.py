'''
Instance Method :
  Key Characteristics of Instance Methods:
    self parameter: The first parameter of an instance method is always self, which refers to the instance of the class.
    Access to instance attributes: Instance methods can access and modify the instance's attributes using self.
    Called on an instance: Instance methods are called on an instance of the class, not on the class itself.
    
When to Use Instance Methods:
    When the method needs to access or modify the instance's state (attributes).
    When the behavior of the method depends on the specific instance.
    For most methods that are tied to the object's data.
    
'''

class Instance:
    def set_instance(self,id,name,age ):
        self.id=id
        self.name=name
        self.age=age
        
    def get_instance(self):
        print(f"Id:{self.id}\nName:{self.name}\nAge:{self.age}")

student_obj=Instance()
student_obj.set_instance(3,"Abhi",22)
student_obj.get_instance()
