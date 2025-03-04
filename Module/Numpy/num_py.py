'''
1. What is NumPy ?
    - Numpy is python library .
    - Numpy is used for working with arrays.
    - Numpy is short name for "Numerical Python ".
    - Numpy was created in 2005 by Travis Oliphant.
    - Numpy is open source.
    
2.Why Use NumPy.
    - Numpy is 50x faster than traditional Python List.
    - Array Object in NumPy is called ndarray .
    - Numpy written using python ,c and c++.

3.Installation of Numpy .
    -If you have Python and Pip already install on a system.
        - pip install numpy.
    - for use numpy u need to import it.
        - import numpy 
'''



#simple example of numpy array.
'''
Numpy is usually import under the np alias.
    -alias in python are an alternative name for refferring to the same thing.
    import numpy same as 
    import numpy as np 
'''
import numpy as np
# import numpy

#we can use whatever we like to use.
# arr=numpy.array([1,2,3,45])
# print(arr)

arr=np.array([1,2,3,45])
print(arr)



#cheking the version of the numpy
print("----------Version of numpy -------------------")
print(np.__version__)