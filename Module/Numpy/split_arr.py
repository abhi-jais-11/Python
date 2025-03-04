import numpy as np


'''
Splitting :
    - Its is ths reverse of the joining.
    - In this brecks sinle the array in multple arrays.
    - array_split() use fro split the array.
    - we also have split() but it fails to adjust the element .
    
'''

#simple array split example

arr=np.array([1,2,3,4,5,6,7,8,9,10])

print("Before Split Array:",arr)

arr=np.array_split(arr,3)

print("After Split Array:",arr)

print("Array 1:",arr[0])
print("Array 2:",arr[1])
print("Array 3:",arr[2])
print('--------------------------')



#2D array split

arr=np.array([[1,2,3],[4,5,6],[7,8,9],[9,8,7]])

print("Before Split Array:",arr)

arr=np.array_split(arr,3)

print("After Split Array:\n",arr)

print("Array 1:",arr[0])
print("Array 2:",arr[1])
print("Array 3:",arr[2])
print('--------------------------')


#2D array hsplit() -> opposite of hstack

arr=np.array([[1,2,3],[4,5,6],[7,8,9],[9,8,7]])

print("Before Split Array:",arr)

arr=np.hsplit(arr,3)

print("After Split Array:\n",arr)

print("Array 1:",arr[0])
print("Array 2:",arr[1])
print("Array 3:",arr[2])
print('--------------------------')


#2D array dsplit() --> opposite of dstack #work on 3 or more dimensions
#vsplit () -> opposite of the vstack.