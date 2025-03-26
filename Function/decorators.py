'''
Decorators in Python
    In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods, without changing their actual code.
    A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
    Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

Syntax of Decorator Parameters
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Add functionality before the original function call
        result = func(*args, **kwargs)
        # Add functionality after the original function call
        return result
    return wrapper

#calling decorators
@decorator_name
def function_to_decorate():
    # Original function code
    pass
    
    Explanation of Parameters
1. decorator_name(func):

decorator_name: This is the name of the decorator function.
func: This parameter represents the function being decorated. When you use a decorator, the decorated function is passed to this parameter.
2. wrapper(*args, **kwargs):

wrapper: This is a nested function inside the decorator. It wraps the original function, adding additional functionality.
*args: This collects any positional arguments passed to the decorated function into a tuple.
**kwargs: This collects any keyword arguments passed to the decorated function into a dictionary.
The wrapper function allows the decorator to handle functions with any number and types of arguments.
3. @decorator_name:

This syntax applies the decorator to the function_to_decorate function. It is equivalent to writing function_to_decorate = decorator_name(function_to_decorate)

'''
'''
Type of decorators.
    1.Function Decorators:
            The most common type of decorator, which takes a function as input and returns a new function. 
            The example above demonstrates this type.
    2. Method Decorators:
            Used to decorate methods within a class. They often handle special cases, such as the self argument for instance methods.
    3.Class Decorators
            Class decorators are used to modify or enhance the behavior of a class. Like function decorators, class decorators are applied to the class definition. They work by taking the class as an argument and returning a modified version of the class.

'''


#1.simple function decorator

def simple_decorator(func):
    def wrapper():
        func()
    return wrapper


@simple_decorator
def greet():
    print("Hello Simple Decorator")
greet()


print('----------------------------------------')

#2.Method Decorator

def method_decorator(func):
    def wrapper(self,*args,**kwargs):
        print("Before")
        func(self,*args,**kwargs)
        print("After")
    return wrapper


class MethodDecorator:
    @method_decorator
    def methodDecorator(self):
        print("This is Method Decorator!")
        

md=MethodDecorator()
md.methodDecorator()


print('--------------------------------------------')
#class decorator

def class_decorator(self):
    name=f"Class Decorators"
    print(name)


@class_decorator 
class Class_Decorator:
    pass


