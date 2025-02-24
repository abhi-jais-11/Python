'''
Type Casting a Variable
    -Type casting refers to the process of converting the value of one data type into another. 
    -Python provides several built-in functions to facilitate casting, including int(), float() and str() among others.
Basic Casting Functions
    -int() – Converts compatible values to an integer.
    -float() – Transforms values into floating-point numbers.
    -str() – Converts any data type into a string.
'''
print("------------------------------Typecasting---------------------------------")
strn='10' # string 
num=int(strn) # convert into integer 
num2=float(strn) # convert into float
age=20 #integer
strg=str(age) # convert into string

print(strn)
print(num)
print(num2)

'''
Getting the Type of Variable
    -In Python, we can determine the type of a variable using the type() function. 
    -This built-in function returns the type of the object passed to it.

'''
print("------------------------------TypeChecking---------------------------------")
print ( type(num)) # <class 'int'>
print(type(num2)) # <class 'float'>
print(type(strg)) # <class 'str'>
print(type(None)) #<class 'NoneType'>




'''

Scope of the variable?
    -There are two methods how we define scope of a variable in python which are local and global.

1.Local  Varianle
2.Global Variable

'''
print("------------------------------Scope of varibale ---------------------------------")
'''
1.Local Variable :
    - If a varibale define iside the function or block  called the local variable.
    - It can access only iside the function or block .
    - It will give an error when i am accessing outside of the function.
'''
def function():
    local_variable="Local Variable"
    print(local_variable)

function()
# print(local_variable)  NameError: name 'local_variable' is not defined.


'''
2.Global Variable
    - Variables defined outside any function are global and can be accessed inside functions and overall file.
'''

global_variable="Global Variable"

def function_Global():
    print("Inside The function",global_variable)

function_Global()
print("Outside of the function",global_variable)


'''
How to convert a local variable into global varibale?
    - we can use global keyword to convert local varibale into global .

'''

def local_to_global_varibale():
    global name
    name="Local And Global "
    print("Inside the function",name)
    
local_to_global_varibale()
print("Outside the function",name)