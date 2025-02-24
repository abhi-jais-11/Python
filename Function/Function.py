'''
Python Functions
    -Python Functions is a block of statements that return the specific task. 
    -The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
Some Benefits of Using Functions
    Increase Code Readability 
    Increase Code Reusability
Types of Functions in Python
    Below are the different types of functions in Python:
    Built-in library function: These are Standard functions in Python that are available to use.
    User-defined function: We can create our own functions based on our requirements.

'''

'''
Creating a Function in Python
    We can define a function in Python, using the def keyword.
    We can add any type of functionalities and properties to it as we require.
    By the following example, we can understand how to write a function in Python. 
    In this way we can create Python function definition by using def keyword.
'''

'''
Syntax:
    def functionName(parameter1,parameter2,......):
         """Docstring"""
        # body of the function
        return expression
            #does not execute after the return 
        
    #function call
    functionName(parameterValue,.......)
'''


#creating sinple function. witghout argument 

def greet():
    print("Hello Welcome !")

greet()


#simple function  with argument
def sum(a,b):
    print(f"Sum is:{a+b}")

sum(10,20)
    
    
    
# simple function with return type 

def is_even(num):
    if num % 2==0:
        return "Even"
    return "Odd"

print(f"Number Is :{is_even(10)}")
print(f"Number Is :{is_even(5)}")


'''
How to access docstring
    print(function_name.__doc__)

'''

def doc_str():
    '''
    This is docstring of the function.
    '''
print(doc_str.__doc__)