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




''''

Type of data type casting:
    
    1.Implicit type casting:
    2.Explicit type casting:

'''


#implicit type casting: it is done by the python interpreter.
#ex:

num1=10 #int
num2=20.5 #float

sum=num1+num2 #float It's  done by python this type of casting known as the inplicit casting.

print('--------------------------------------')
print(sum,type(sum))


num_str='10' #string data type
print(type(num))
num=int(num_str)   # converting string to integer forcefully by the user this type of conversion known as the explicit conversion.
print(num,type(num))