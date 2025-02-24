'''
Python Tuples
    -A tuple in Python is an immutable ordered collection of elements. 
    -Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable). -Tuples can hold elements of different data types. 
    -The main characteristics of tuples are being ordered , heterogeneous and immutable.


'''

'''
1.Creating a Tuple
A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items and they can be of different data types.

'''
tup=()
print(type(tup))

# tuple with integer value 
tup=(1,2,3,4,5,6,7,8,9)
print(tup)


#tuple with mixexd value
tup=('jack',10,2+3j)
print(tup)

print('---------------------------')

'''
2.Python Tuple Operations
Below are the Python tuple operations.
    -Accessing of Python Tuples
    -Concatenation of Tuples
    -Slicing of Tuple
    -Deleting a Tuple
'''
#accessing the tuple 

tup=(1,2,3,4,5,6,7,8)
print(tup[0])
print(tup[6])


# accessing using loop

for i in tup:
    print(i,end=" ")
print()

print('--------------------------')

#concatenation of the tuple 
tup = tup+(9,20,10)
print(tup)

tup=tup+('jack','mice',)
print(tup)


print('-----------------------------')

#slicing of tuple 

print(tup[0:])
print(tup[1:5])
print(tup[1:8:2])
print(tup[::-1])
print(tup[-8:-1])


print('---------------------------')
del tup
# print(tup)  nameerror