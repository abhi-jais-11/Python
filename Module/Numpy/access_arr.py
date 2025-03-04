import numpy as np

'''   
 1.Accessing the element of the array.
    - Array use indexing . 
    - We can access the element of the array by using the index.
    - In general the index start form 0 and end with n-1.
    - Where the n is number of the element in the array.

        ex.
            arr=[1,2,3,4,5]
                - Size and Number of element = 5
                - Index start from 0 and end with n-1 = 0 to 4 index

'''

#accessing the element of the array

# 0-D

arr=np.array(42)
print("Value of the Array:",arr) #there no index it will give an error while aceess using index bcz of 0-d and single element
print('-----------------------------------')


# 1-D

arr=np.array([1,2,3,4,5])
print(f"The Value Of the Element At the Index of {0} : {arr[0]}")

print('----------------------- 1D Array ------------------------------')
#using the loop 
for x in arr:
    print(f"The value of the array: {x}")
    
print('-------------------------------------------------------')


# 2-D array

arr=np.array([[1,2,3,4,5],[5,4,3,2,1]])
print(f"The Value Of the Element At the Index of {1} {1} : {arr[1][1]}")

print('------------------------ 2D Array -----------------------------')
#using the loop 
for x in arr:
    for y in x:
        print(f" The value of the array : {y}")
    
print('------------------------- 3D Array ------------------------------')

# 3-D


arr=np.array([[
    [1,2,3],
    [5,4,3] 
    ]])

# using loop

for x in arr:
    for y in x:
        for z in y:
            print(f"Value of the Array:{z}")
            
            
print('-------------------------------------')


'''

Enumarate Access With The Index.


'''

for idx,val in np.ndenumerate(arr):
    print(f"Value At The Index {idx}={val}")

print('-------------------------------------')