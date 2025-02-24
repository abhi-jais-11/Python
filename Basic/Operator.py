'''
Python Operators
     -In Python programming, Operators in general are used to perform operations on values and variables. 
     -These are standard symbols used for logical and arithmetic operations.
     OPERATORS: These are the special symbols. Eg- + , * , /, etc.
     OPERAND: It is the value on which the operator is applied.

'''

'''
There are the list of the operator inside the function.
    1.Arithmetic
    2.Assignment
    3.Bitwise
    4.Comparison
    5.Logical
    6.Identity
    7.Membership

'''

'''
1.Arithmetic Opertor
    -It is use to perform the mathmetical opertaion -> addition subtraction... etc.
    1.+ Addition 
    2.- Subtraction
    3.* Multiplication 
    4./ Division
    5.// FloorDivision Always retur integer value 
    6.% Modulus
    7.** Exponential use to calculate the powers
'''
a=10
b=5
print("a=",a)
print("b=",b)
print("---------------------------------Arithmetic Operator --------------------------------------")
print(f"Sum of {a} + {b} = {a+b}")
print(f"Sub of {a} - {b} = {a-b}")
print(f"Mul of {a} * {b} = {a*b}")
print(f"Div of {a} / {b} = {a/b}")
print(f"floor Div of {a} // {b} = {a//b}")
print(f"Modulus of {a} % {b} = {a%b}")
print(f"Exponential of {a} ** {2} = {a**2}")

'''
1.Assignment Opertor
    -It is use to perform the mathmetical opertaion -> addition subtraction... etc.
    1.+= Addition 
    2.-= Subtraction
    3.*= Multiplication 
    4./= Division
    5.//= FloorDivision Always retur integer value 
    6.%= Modulus
    7.**= Exponential use to calculate the powers
'''
print("---------------------------------Assignment Operator --------------------------------------")
b+=5
print("The value of b+=5-> b=b+5 ",b)
b-=5
print("The value of b-=5",b)
b*=5
print("The value of b*=5",b)
b/=5
print("The value of b/=5",b)
b//=5
print("The value of b//=5",b)
b%=5
print("The value of b%=5",b)
b**=5
print("The value of b**=5",b)

print("---------------------------------Bitwise Operator --------------------------------------")
'''
1.Bitwise Opertor
   1 ~ Bitwise NOT
   2 >> << Bitwise Shift
   3 & Bitwise AND
   4 ^ Bitwise XOR
   5.| Bitwise OR
'''
x=1
y=0
print("x & y",x&y)
print("x | y",x|y)
print("x ^ y",x^y)
print("~y",~y)
print("4>>2",4>>2)
print("4<<2",4<<2)
print("5<<2",5<<2) 
print("5>>2",5>>2)


print("---------------------------------logical Operator --------------------------------------")
'''
1.Bitwise Opertor
   1. and 
   2. or 
   2. not 
'''
print(1 and 1)
print( 1 or 0)
print(1 and 0)
print( 1 or 1)
print( not 0)


print("---------------------------------Membership Operator --------------------------------------")
'''
1.Bitwise Opertor
    1.in  True if value is found in the sequence
    2.not in  rue if value is not found in the sequence

'''
print(2 in [1,2 ,3,4])
print(2 not in [1,2 ,3,4])
print(10 in [1,2,3,4,5])
print( 10 not in [1,2,3,4])


print("---------------------------------Identity Operator --------------------------------------")
'''
1.Bitwise Opertor
    1.is  True if value is found in the sequence
    2.is not   rue if value is not found in the sequence

'''
print([] is [] )
print({} is not {})
a=[]
b=a
print(a is b)
print(a is not b) 