'''
Inside a class, we can have three types of variables. They are:

Instance variables (object level variables)
Static variables (class level variables)
Local variables (method level)

'''

'''
If the value of a variable is changing from object to object then such variables are called as instance variables.
Where instance variables can be declared?
We can declare and initialize the instance variables in following ways,

By using a constructor.
By using instance methods.
By using object name
'''

class IncetanceVarible:
    
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        print("Initializtion and Declaration fo the Inctance Varibale")
        print(f"Instance Varibale Using Contructor :\nid:{self.id}\nName:{self.name}\nAge:{self.age}")
        print('-------------------------------')
        
    #using instance method 
    
    def instance_method(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        print(f"Instance Varibale Using Instance Method [self]  :\nid:{self.id}\nName:{self.name}\nAge:{self.age}")
        print('-------------------------------')
        
        

InstanceVar=IncetanceVarible(3,"jacksone",23)
InstanceVar.instance_method(3,"jacksone",23)
iv=InstanceVar
iv.id=4
iv.name="Jack"
iv.age=33
print(f"Instance Varibale Using Object  :\nid:{iv.id}\nName:{iv.name}\nAge:{iv.age}")
print('-------------------------------')
print("Accessing  the Inctance Varibale")
print(f"Instance Varibale Using Object  :\nid:{iv.id}\nName:{iv.name}\nAge:{iv.age}")
iv.instance_method(4,"Rahul",26)




'''
Static Variables in Python
If the value of a variable is not changing from object to object, such types of variables are called static variables or class level variables. 
We can access static variables either by class name or by object name.
Accessing static variables with class names is highly recommended than object names.


'''

class StaticVaribale:
    #static varibale direct inside the class
    colleg_name="Class BIET" # not change  for studnts to students 
    print(colleg_name)
    
    #static valribale using constuctor 
    
    def __init__(self):
        StaticVaribale.colleg_name="Contsructor BIET"
        print(StaticVaribale.colleg_name)
        
    
    
    #static varibale using instance method 
    
    def instance_method(self):
        StaticVaribale.colleg_name="Instance Method BIET"
        print(StaticVaribale.colleg_name)
        
    
    @classmethod 
    def class_method(cls):
        StaticVaribale.colleg_name="Class Method BIET"
        print(StaticVaribale.colleg_name)
     
    @staticmethod
    def static_method():
        StaticVaribale.colleg_name="Static  Method BIET"
        print(StaticVaribale.colleg_name)


sv=StaticVaribale()
sv.instance_method()
sv.static_method()
StaticVaribale.class_method()

print('-----------------------------------------------')
        
        
class LocalVaribale:
    def local_varible(self):
        local_var="This is Local Varibale:"
        print(local_var)
        

lv=LocalVaribale()
lv.local_varible()