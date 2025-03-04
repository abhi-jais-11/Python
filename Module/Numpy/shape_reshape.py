import numpy as np

'''
shape of array :
        - Number of the element in each dimension.

'''
arr=np.array([1,2,3],ndmin=5)
print("------------------- shape of the array -----------------------")
print(arr.shape)
print("------------------------------------------")



arr=np.array([
    1,2,3,4,5,6,7,8,9,0,10,12
])
print("Before Reshape:",arr)
new_arr=arr.reshape(2,3,2) # 2arr 3D 2row
print("After Reshape:",new_arr)
'''





'''