'''
Copy () and View ()

    - The main defference between a copy and a view of an array is.
    - That the copy is a new array and the view is just a view of original array.
    - Copy owns data and any change nade to the copy will not affect the original array .
    - Any change on the original array will not affect the copy .
    
    - The view does not own the data and any change mode to the view will affect the array.
    -  Any change on the original array will  affect the view .

'''

#copy()

import numpy as np

arr=np.array([1,2,3,4,5])
copy_array=arr.copy()

print("Original Array:",arr)
print('---------------------------')
print("Copy Array:",copy_array)
print("----------------Modifying The both Array Copy() -------------------")
arr[0]=10
copy_array[0]=30
print("Original Array:",arr)
print('---------------------------')
print("Copy Array:",copy_array)



#view()
arr=np.array([1,2,3,4,5])
view_array=arr.view()

print("Original Array:",arr)
print('---------------------------')
print("Copy Array:",view_array)
print("----------------Modifying The both Array View() -------------------")
arr[0]=10
view_array[0]=30
print("Original Array:",arr)
print('---------------------------')
print("Copy Array:",view_array)


print('------------------Check If Array Owns Data ---------------------')
print("For Copy :",copy_array.base)

print("For View :",view_array.base)




