'''
Types of Python Function Arguments
    Python supports various types of arguments that can be passed at the time of the function call. 
    In Python, we have the following function argument types in Python:
Default argument
Keyword arguments (named arguments)
Positional arguments
Arbitrary arguments (variable-length arguments *args and **kwargs)
'''


'''
1.Default Argument
'''

def def_args(name="Jack",age=21):
    '''
    There are the two default arguments name and age 
    if the user does not pass any value then it will use by the function.
    '''
    print(f"Name:{name} and Age:{age}")

def_args("jackson",29)
def_args()

print('------------------------------------------')
'''
2.Keyword arguments (named arguments)

'''
def key_args(fname,lname):
    print(f"Full Name: {fname +" "+ lname}")
    

# keyword argument
key_args(fname="Rahul",lname="Jawle")


print('------------------------------------------')
'''
3.Positional Arguments
'''

def  pos_args(name,age):
    print(f"Name:{name} and Age:{age}")
    
    
pos_args("Rahul",30)# give right output 
pos_args(30,"Rahul")#give the wrong output bcz change the  order 

print('--------------------------------------')

'''
4.Arbitrary Keyword  Arguments
    In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

*args in Python (Non-Keyword Arguments)
**kwargs in Python (Keyword Arguments)

'''

def args(*args): # can take any number of argument * 
    for _ in args:
        print(_,end=" ")
    print()

args(1,2,2,3,3,3,4,4,4,5)


print('------------------------------------------')

def  kwargs(**kwargs):
    for key,val in kwargs.items():
        print(f" {key} : {val} ")
        

kwargs(name="Rahul" , age=21, address="Mumbai")
        
        
        