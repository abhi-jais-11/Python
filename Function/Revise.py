#
'''
Function :
    syntax:
            keyword    function name     - Arguments....
             |          |               |
            def function_name (arguments...):

                    """ docstrings """
                    
                    #executable code 
                    
                    return statement
            
            #function call
            
            function_name(parameters....)



'''
# simple function without argumnet without return statement

def greet():
    print("Hello Welcome !")

#function call / invoke 
greet()

print('-------------------------------')
# simple function without argumnet with return statement
def greet():
    return "Hello Welcome !"

print(greet())


print('-------------------------------')
# simple function with argumnet without return statement

def greet(name=None):
    if name is not None:
       print(f"Hello Welcome {name} !")
    print(f"Name Can Not None !") 
    
greet("Home")
greet()


print('-------------------------------')
# simple function with argumnet with return statement

def greet(name=None):
    if name is not None:
       return f"Hello Welcome {name} !"
    return f"Name Can Not None !" 
    
print(greet("Home"))
print(greet())


print('---------------------------------------')


def emp_info():
    '''
    This function is create the imployee records Using Id , Name etc.
    '''
    pass
        


#how to access docstring
print(emp_info.__doc__) #return docs




print('--------------------------------------')

'''
Type of Arguments in Function:
    1.Default Arguments
    2.Positional Arguments
    3.Keyword Arguments
    4.Arbitary-Arguments/Varibale length arguments [*args and **kwargs]


'''

#1.default argument

#without default 
# def default_args(name):
#     print(f"Hello Welcome {name}")
    
#with default
def default_args(name="Jack"):
    print(f"Hello Welcome {name}")

'''
  [ a=0 ]default value is 0
'''
def add(a=0,b=0,c=0):
    print(sum([a,b,c]))

    
#calling function
print('-----------------------------------')
default_args("Abhi")
default_args()#it will not give any error because of default argument if we are not use defualt argument give an error.
#TypeError: default_args() missing 1 required positional argument: 'name'

print('--------------------------------------')
#calling sum
add(10,20,20)
add(10,20)
add(10)
print('-----------------------------------')


#2.Positional arguments

def positional_args(name,age):
    print(f"Name:{name} and Age:{age} ")



#calling function
positional_args("jack",22)
print('-------------------------')
positional_args(22,"Jack") #if we change the order of the parameter it will give  wrong output 

print('------------------------------------------')
# positional_args() #if we calling the function without value it w'll  give an error TypeError.


#for solving this type of proble we can use the type of the argument

def positional_args(id:int,name:str,age:int)->None:
    try:
        assert isinstance(id,int) and isinstance(name,str) and isinstance(age,int)
    except:
        print(f"Give The Proper Value Type :")
    else:
       print(f"Id:{id} ,Name:{name} and Age:{age}")
       

positional_args(10,"Jacksone",23)
print('-----------------------------')

positional_args(11,"Jacksone",20) # if we change the order it will give an error



print("-------------------------------------")
#To solve the Order Proble We have third type of arguments

#3.Keyword arguments

def keyword_args(id,name,age,email):
    print(f"Id:{id} and Name:{name} , Age:{age} and Email:{email} ")


keyword_args(email="jack12@gmail.com",age=22,name="Jacksone",id=10) #keyword argumnet
keyword_args(id=11,name="Jack",age=23,email="jck1228@gmail.com") # we can change the order 


print("-------------------------------------")



#4.varibale length arguments

        #1.*Args [positional variable legnth args  ]
        #2.**kwargs [keyword variable legnth args]
    


#1.*args

def args(*args):
    return sum(args)


print(args(1,2,2,0,202,20)) #can take any no of args
print('-----------------')
print(args(10,20,30))
print('-----------------')
print(args(10,20))

print('------------------------------------------')

#2.Varibale length keyword argument
 
def kwargs(**kwargs):
#    print(kwargs)
   for k,v in kwargs.items():
       print(f"{k.capitalize()}:{v}")


kwargs(email="jack12@gmail.com",age=22,name="Jacksone",id=10) 
print('------------------------------------')
kwargs(id=11,name="Jack",age=23,email="jck1228@gmail.com") 

#kwargs("jack",22) #TypeError: kwargs() takes 0 positional arguments but 2 were given [ it can not take positional args ]
print('---------------------------------------------------')