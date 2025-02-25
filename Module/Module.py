'''
A module in Python is a file that contains Python code, such as functions, classes, variables, and definitions. Modules are similar to code libraries. 
Benefits of using modules
    Organization: Modules help organize code into logical groups, making it easier to understand and use. 
    Reusability: Modules can be imported into other programs, allowing code to be reused. 
    Simplicity: Modules can focus on a small portion of a problem, making development easier. 
    Maintainability: Modules can enforce logical boundaries between different problem domains. 
Creating modules 
    To create a module, save the code you want to use in a file with the extension .py.
For example, you can create a module named mymodule.py.
    Importing modules 
    You can import modules into other modules or into the main part of the program using the import statement.

Type of Module 
    1.userdefine module
    2.built-in module
'''


# creating a calculator function

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b!=0:
        return a/b
    else:
        return f"Zero Division Error"
    

def mod(a,b):
    return a%b

def powd(n,p):
    return n**p
    


if __name__=='__main__':
    add()