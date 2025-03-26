'''
what is class ?

    -A class in Python is a user-defined template for creating objects.
    -It bundles data and functions together, making it easier to manage and use them.
    -When we create a new class, we define a new type of object. 
    -We can  create multiple instances of this object type.
    -Classes are created using class keyword.
    -Attributes are variables defined inside the class and represent the properties of the class. 
    -Attributes can be accessed using the dot . operator (e.g., MyClass.my_attribute).
    
    Syntax:
        class class_name:
            #attributes
            #methods
            

whst is object?
    -An Object is an instance of a Class.
    -it represents a specific implementation of the class and holds its own data.

State: 
    It is represented by attributes of an object.
    It also reflects the properties of an object.
Behavior: 
    It is represented by methods of an object. 
    It also reflects the response of an object with other objects.
Identity: 
    It gives a unique name to an object and enables one object to interact with other objects.


    Syntax:
        object_name=Classname()
    
'''

#simple student class

class Student:
    '''
    Class for the student info system.
    '''
    college_name="BIET" #static / class level variable
    
    def __init__(self,id=0,name=None,course=None): #refer to __init__.py
        self.id=id
        self.name=name             #inatance  /object level avriables
        self.course=course
        # self.get_info() valid
        # Student.get_info(self) valid
    
    def get_info(self):
        print(f'''
        ---------------------------------------      
              Id:{self.id}
              Name:{self.name}
              Course:{self.course}
              Colleg:{Student.college_name}
        ---------------------------------------
              ''')
    

#creation of object
student_object=Student(3,"Jack","B.Tech") #initializing instance variabel refer to variable.py
# student_object=Student()#TypeError We can use default parameter in method to remove this error.
# Student.get_info(student_object) valid not recomnded

# student_object.get_info() #recomnded



#how to Access the docstring of the class and information about the class

print(student_object.__doc__) #return the docstring
print("------------------------------")
print(Student.__doc__) #return the docstring
# print("------------------------------")
# help(Student)  #return the structure of the class
# print("------------------------------")
# help(student_object) #return the structure of the class
# print("------------------------------")
# print(dir(student_object)) #return the list of all class methods and the class level varibale and instance varibale
# print(dir(Student)) #return the list of all class methods and the class level varibale

# print(Student.__dict__) #return class information dictionary