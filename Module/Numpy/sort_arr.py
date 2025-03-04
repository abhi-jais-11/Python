import numpy as np

'''

Sorting Array :
    - sorting means putting element in an ordered sequence .
    - aceending or deccending. [ numeric or alphabetic]
    
'''

'''
1.sort() function will sort a specified array

'''

arr=np.array([1,2,3,10,100,4,9,20])
print("Before Sort Array:",arr)
print("After Sort Array :",np.sort(arr)) #return copy of array original array unchange.

print('-----------------------------------------------')


arr=np.array(['banana','cherry','apple','mango'])
print("Before Sort Array:",arr)
print("After Sort Array :",np.sort(arr))

print('-----------------------------------------------')
arr=np.array([True,False,False,True])
print("Before Sort Array:",arr)
print("After Sort Array :",np.sort(arr))

print('-----------------------------------------------')

arr=np.array([[2,4,5,10],[1,2,4,8]])
print("Before Sort Array:",arr)
print("After Sort Array :",np.sort(arr))

print('-----------------------------------------------')