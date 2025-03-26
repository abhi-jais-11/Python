
'''
Public Access Modifier:
    -The members of a class that are declared public are easily accessible from any part of the program.
    -All data members and member functions of a class are public by default. 
'''



class Public:
    
    #public variables 
    college_name="BIET"
    college_add="Lucknow"
    
    #special method called constructor in python
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    
    #public methods
    def get_info(self):
        print("Public Variables Inside of the Class:")
        print(f"Name:{self.name}\nAge:{self.age}\nCollege:{Public.college_name}\nCollegAdd:{Public.college_add}")
        
    
    def set_info(self,name,age,colleg_name,colleg_add):
        Public.college_name=colleg_name
        Public.college_add=colleg_add
        self.__init__(name,age)
        
    



#object  creation

pub_obj=Public("Jack",22)
pub_obj.get_info()
pub_obj.set_info("JackSone",23,"DDU","Delhi")
pub_obj.get_info()

#public varible can access outside of the class but static 
#ex.
print('--------------------------------------')
print("Public Variables Outside of the Class:")
print(f"Name:{pub_obj.name}\nAge:{pub_obj.age}\nCollege:{pub_obj.college_name}\nCollegAdd:{pub_obj.college_add}")

#if we are accessing the instance varibale outside of the class using the class name give an Atrribute error.
# #AttributeError: type object 'Public' has no attribute 'name
# print(f"Name:{Public.name}\nAge:{Public.age}\nCollege:{Public.college_name}\nCollegAdd:{Public.college_add}")
print('--------------------------------------')
print(f"Name:{pub_obj.name}\nAge:{pub_obj.age}\nCollege:{Public.college_name}\nCollegAdd:{Public.college_add}")