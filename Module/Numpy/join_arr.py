import numpy as np

'''

Joining :
    - Joining means the putting the contents of two or more arrays in single array.
    - Join in numpy arrays by using the axes.
    - We pass the sequence of the arrays that we want to join .


'''

'''
1.concatenate()  If axis is not explicitly passed It is  taken as 0.


'''

arr_one=np.array([1,2,3])
arr_two=np.array([4,5,6])

arr=np.concatenate((arr_one,arr_two))

print(f"Array After joind:{arr}")


# 2D array joining axis = 1 row
print('--------------------------------')

arr_one=np.array([[1,2,3],[3,2,1]])
arr_two=np.array([[4,5,6],[6,5,4]])

arr=np.concatenate((arr_one,arr_two), axis=1)

print(f"Array After joind:{arr}")




'''
1.stack()  If axis is not explicitly passed It is  taken as 0. It is same as the concatenat() 
           Only defference is that the concatenation done with a new axis.


'''
print('---------------------------------')
arr_one=np.array([1,2,3])
arr_two=np.array([4,5,6])

arr=np.stack((arr_one,arr_two),axis=1)

print(f"Array After joind:{arr}")




'''
1.hstack()  Numpy Provide the helper function : to stack along rows.

'''
print('---------------------------------')
arr_one=np.array([1,2,3])
arr_two=np.array([4,5,6])

arr=np.hstack((arr_one,arr_two))

print(f"Array After joind:{arr}")

'''
1.vstack()  Numpy Provide the helper function : to stack along columns.

'''
print('---------------------------------')
arr_one=np.array([1,2,3])
arr_two=np.array([4,5,6])

arr=np.vstack((arr_one,arr_two))

print(f"Array After joind:{arr}")


'''
1.dstack()  Numpy Provide the helper function : to stack along height.

'''
print('---------------------------------')
arr_one=np.array([1,2,3])
arr_two=np.array([4,5,6])

arr=np.dstack((arr_one,arr_two))

print(f"Array After joind:{arr}")

