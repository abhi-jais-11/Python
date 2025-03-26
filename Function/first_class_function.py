''''
First Class functions in Python
     This means that functions in such languages are treated like any other variable. 
     They can be passed as arguments to other functions, returned as values from other functions, assigned to variables and stored in data structures.
Characteristics of First-Class Functions
     Assigned to Variables: We can assign functions to variables.
     Passed as Arguments: We can pass functions as arguments to other functions.
     Returned from Functions: Functions can return other functions.
     Stored in Data Structures: Functions can be stored in data structures such as lists, dictionaries, etc.
'''

'''
Assigning Functions to Variables
     We can assign a function to a variable and use the variable to call the function.
'''

def square(n):
    return n**2
sq=square
print("The square of the number is :",sq(10))

print('----------------------------')

'''
Passing Functions as Arguments
    Functions can be passed as arguments to other functions, enabling higher-order functions.

'''

def greet(name):
    return f"Hello {name}"

def main(function,name):
    return function(name)


name=main(greet,"Jacksone")
print(name)

print('-----------------------------------')

'''
Returning Functions from Other Functions
    A function can return another function, allowing for the creation of function factories.


'''
def outer(msg):
    def inner():
        return f"Message: {msg}"
    return inner

func = outer("Hello, World!")
print(func()) 