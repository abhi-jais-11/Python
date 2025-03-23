'''
Python Exception Handling
    Python Exception Handling handles errors that occur during the execution of a program.
    Exception handling allows to respond to the error, instead of crashing the running program. 
    It enables you to catch and manage errors, making your code more robust and user-friendly.

Syntax and Usage
Exception handling in Python is done using the try, except, else and finally blocks.

try:
      # Code that might raise an exception
except SomeException:
      # Code to handle the exception
else:
     # Code to run if no exception occurs
finally:
    # Code to run regardless of whether an exception occurs
    
    
try, except, else and finally Blocks
    try Block: try block lets us test a block of code for errors.
    Python will “try” to execute the code in this block. 
    If an exception occurs, execution will immediately jump to the except block.
    
    except Block: except block enables us to handle the error or exception.
    If the code inside the try block throws an error, Python jumps to the except block and executes it. 
    We can handle specific exceptions or use a general except to catch all exceptions.
    
    else Block: else block is optional and if included, must follow all except blocks.
    The else block runs only if no exceptions are raised in the try block.
    This is useful for code that should execute if the try block succeeds.
    finally Block: finally block always runs, regardless of whether an exception occurred or not. 
    It is typically used for cleanup operations (closing files, releasing resources).

'''

#simple example :

def exception_handling(a,b):
    
    try:
        res=a/b
        
    except ZeroDivisionError as e:
        print(f"{e} You can't divide by zero!")
    
    else:
        print("Division Of the Numbers is :",res)
    
    finally:
        print("Execution complete.")


n=int(input("Enter The Number 1st:"))
m=int(input("Enter The Number 2nd:"))
exception_handling(n,m)
    
        
        
        
    