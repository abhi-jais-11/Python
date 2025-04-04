'''
Python Variables?
    -In Python, variables are used to store data that can be referenced and manipulated during program execution.
    -A variable is essentially a name that is assigned to a value. 
    -Unlike many other programming languages, Python variables do not require explicit declaration of type. 
    -The type of the variable is inferred based on the value assigned.

'''

'''
Rules for Naming Variables
    - Variable names can only contain letters, digits and underscores (_).
    - A variable name cannot start with a digit.
    - Variable names are case-sensitive (myVar and myvar are different).
    - Avoid using Python keywords (e.g., if, else, for) as variable names.
    1.valid ex:
    - name="Jackson"
    - name_of_of="Jackson"
    - name_="Jackson"
    - age1="Jakc21"
    - Hell_Hii="Hello"
    
    2.not valid eX:
    - 2name="jakcson"
    - name age ="102"
    - $name="Not valid "

'''


'''
Assigning Values to Variables

'''
name_="jack"
num=10
f_num=13

'''
Multiple Assignments
Python allows multiple variables to be assigned values in a single line.

'''
a=b=c=100

'''
Assigning Different Values

'''
name,age,sallary="Abhinav Jaiswal ",23,"200k"



'''
Object Reference in Python

x=5 
y=x then x=y=5

x="jack"
the x=jack and y=5

and y="jackson"

then x="jack" and y="jackson" ==> 5->garbage
'''
x=5 
y=x 
print(x,y)
x="jackson"
print(x,y)
y="jack"
print(x,y)




'''
Delete a Variable Using del Keyword
We can remove a variable from the namespace using the del keyword.
This effectively deletes the variable and frees up the memory it was using.

'''
# Assigning value to variable
x = 10
print(x) 

# Removing the variable using del
# del x

print(x) # NameError: name 'X' is not defined


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