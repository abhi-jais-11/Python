'''
Method Overloading:
    Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. These methods are called overloaded methods and this is called method overloading. 

    -Python does not support method overloading by default. 
    -But there are different ways to achieve method overloading in Python. 


'''

#simple function

class MethodOverloading:
    
    def sum(self,a,b):
        print(f"Sum of the Numbers is:{a+b}")
    
    def sum(self,a,b,c):
        print(f"Sum of numbers is :{a+b+c}")
        

over=MethodOverloading()
# over.sum(10,20) #TypeError: MethodOverloading.sum() missing 1 required positional argument: 'c'
over.sum(10,20,30)


#solving the problem using  *Args

class MethodOverloading:
    
    def sum(self,a,b):
        print(f"Sum of the Numbers is:{a+b}")
    
    def sum(self,*args):
        print(f"Sum of numbers is :{sum(args)}")
    
    
print("_---------------Solve using *args -------------------------_")

over=MethodOverloading()
over.sum(10,20) 
over.sum(10,20,30)



#solve this problem using the deafults parameter

class MethodOverloading:
    
    def sum(self,a,b):
        print(f"Sum of the Numbers is:{a+b}")
    
    def sum(self,a,b,c=0):
        print(f"Sum of numbers is :{a+b+c}")
        

print("_---------------Solve using default parameter --------------_")
over=MethodOverloading()
over.sum(10,20) 
over.sum(10,20,30)






