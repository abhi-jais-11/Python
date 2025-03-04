'''
Create randome array :
    -Numpy work with the array and you can use method to make random array .

'''

'''
Integers:   
    - randomint() 
        - take the size parameter where you can specify the shape of the array.
         
'''
from numpy import random

#one d
arr=random.randint(100,size=(5))
print(arr)

print("---------------------------")

arr=random.randint(100,size=(3,3))
print(arr)

print("---------------------------")

'''
Floats:   
    - rand() 
        - take the rand(3,3) parameter where you can specify the shape of the array.
         
'''

print("---------------------------")

arr=random.rand(3,3)*10
print(arr)

print("---------------------------")


'''
Choice() :
    - method also return arrays values.
        - add a size parameter to specify shape of the array.
        
         
'''


print("---------------------------")

arr=random.choice([1,2,3,4,5,6,7,8],size=(3,3))
print(arr)

print("---------------------------")

