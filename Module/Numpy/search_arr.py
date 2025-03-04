import numpy as np

'''
You can search an array for a certain value and return the indexes that get match .

'''

'''
1.Where() method it work like sql  where .


'''

arr=np.array([10,20,5,4,6,9,4])
print(np.where(arr == 4)) #return the array of  indexex  of the element

print('------------------------')

'''
find the index where the value is even

'''
print("Even Values Index of the Array:",np.where(arr%2==0))

print('------------------------------')

print("Odd Values Index of the Array:",np.where(arr%2!=0))


'''

searchsorted()
        -This performs a binary search in the given array and returns the index .
        -where the specified value would be inserted to maintain the search order.
        - Array should be in sorted array.      
'''

print('---------------------------------------')
arr=np.array([1,2,3,4,10,29,30,49,50,54])
x=49
print(f"The value {x} at the index: {np.searchsorted(arr,x)}")

print('------------------------------------------')
arr=np.array([1,2,3,4,10,29,30,49,50,54])
x=[1,29,54] #multiple values
print(f"The value {x} at the index: {np.searchsorted(arr,x)}")
