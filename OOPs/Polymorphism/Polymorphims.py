'''
Polymorphism
    -Polymorphism is a foundational concept in programming that allows entities like functions, methods or operators to behave differently based on the type of data they are handling. 
    -Derived from Greek, the term literally means “many forms”.
    -Python’s dynamic typing and duck typing make it inherently polymorphic.

'''


'''
Polymorphism in Built-in Functions
        -Python’s built-in functions exhibit polymorphism, adapting to various data types.
'''

print('----------------Built-in Function Polymorphism ------------------')

print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length
print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings

#Python determines behavior at runtime, enabling these functions to work across diverse types without explicit type declarations.


'''
Polymorphism in Functions
        -Duck typing enables functions to work with any object regardless of its type.

'''

print('---------------Function Polymorphism ------------------')

def add(a, b):
    return a + b

print(add(3, 4))           # Integer addition
print(add("Hello, ", "World!"))  # String concatenation
print(add([1, 2], [3, 4])) # List concatenation



'''
Polymorphism in Operators
Operator Overloading
   In Python, operators like + behave polymorphically, performing addition, concatenation or merging based on the data type.

'''
print('---------------Function Polymorphism ------------------')

print(5 + 10)  # Integer addition
print("Hello " + "World!")  # String concatenation
print([1, 2] + [3, 4])  # List concatenation



'''
Types of Polymorphism

    Compile-time Polymorphism
            In Python, which is dynamically typed, compile-time polymorphism is not natively supported. Instead, Python uses techniques like dynamic typing and duck typing to achieve similar flexibility.
            method overloading
            
    Runtime Polymorphism
            Occurs when the behavior of a method is determined at runtime based on the type of the object.
            In Python, this is achieved through method overriding: 
            A child class can redefine a method from its parent class to provide its own specific implementation.
            Python’s dynamic nature allows it to excel at runtime polymorphism, enabling flexible and adaptable code.
            method overriding
'''