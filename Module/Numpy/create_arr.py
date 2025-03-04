import numpy as np 

'''
Numpy is use to work work with arrays .
    the array object in numpy is called ndarray.


'''

#for creasion of the array the array() use .

arr=np.array([1,2,3,3]) #oned Array
print(arr)
print('----------------------------------')
'''
Type of the dimensions in Numpy.
    1. 0-D
    2. 1-D
    3. 2-D [multi]
    4. 3-D [multi] ...so on

for check the dimension of the array we use [ndim]

'''

# 0-D
zero_d=np.array(46)
print(zero_d)
print("Dimensions:",zero_d.ndim)

print('----------------------------------------------')
#1-D
one_d=np.array([1,2,3])
print(one_d)
print("Dimensions:",one_d.ndim)

print('----------------------------------------------')

# 2-D
two_d=np.array([[1,2,3] , [1,2,3] ])

print(two_d)
print("Dimensions:",two_d.ndim)

print('----------------------------------------------')
# 3-D
three_d=np.array([[[1,2,3],[1,3,3],[1,2,3]]])

print(three_d)
print("Dimensions:",three_d.ndim)

print('----------------------------------------------')



'''

Cresion of the Higher Dimension array.
    - An array can have any number of dimensions .
    - we can define dimensions of the array bu using the[ ndmin ]

'''

#simple example 

nd_array=np.array([1,2,3,4,5],ndmin=5)
print(nd_array)
print("Dimensions:",nd_array.ndim)
print('----------------------------------------------')