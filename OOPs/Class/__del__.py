'''
Destructors:
    -Destructors are called when an objectct gets destroyed.
    -In python destructors are not nedded as much as in c++.
    -python has the garbage collectorthat handles memory management.
    nn nnn 
The __del__() :
        -Method is know as a destructor method in Python .
        - It called when all references to the object have been deleted.
        - It called  after the program ended .
        
        Syntax:
            -def __del__(self):
                #body


'''

#simple example

class Student:
    
    def __init__(self):
        print("Student Class !")
        print(id(self))
        
    def __del__(self):
        print("Student Class Delete !")


# student_obj=Student()
# print(id(student_obj))
# del student_obj
# print(id(student_obj)) # NameError: name 'student_obj' is not defined

        
# example to destructors whet it execute ..

class Recursive_Num:
    sum=0
    def  run(self,n):
        self.n=n
        if self.n <=0:
            return 
        else:
            self.sum+=self.n
            print("The Value Of N=",self.n,"Sum OF the Nums is :",self.sum)
            self.run(self.n-1)
    def __del__(self): 
        print("End Of the Program!") #execute after the end of the run function.
        self.get_obj()
    
    def get_obj(self):
        print("Object Is :",self)        

rcv_obj=Recursive_Num()
rcv_obj.run(5)
#destroy the object 
print("{:x}".format(id(rcv_obj)).upper())
del rcv_obj

