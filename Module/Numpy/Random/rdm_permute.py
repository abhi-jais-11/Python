from numpy import random
import numpy as np
'''

A permutation  refers to an arrangement of elements.
    - ex.   [3,2,1]-[1,2,3]

and vice-vers.


'''


'''
The numpy reandom module provides two methods for this .
    -suffle() - it makes changes in the original array.
    -permutation() - it's not make change in original array.

'''


arr=np.array([1,2,3,4,5])

print("Before Arrange:",arr)

#using the suffle
random.shuffle(arr)

print("After Arrange :",arr)



print('-----------------------------')
arr=np.array([1,2,3,4,5])

print("Before Arrange:",arr)

#using the permutaion
arr=random.permutation(arr)

print("After Arrange :",arr)
