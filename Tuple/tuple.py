'''
Python Tuples
    -A tuple in Python is an immutable ordered collection of elements. 
    -Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
    -Tuples can hold elements of different data types. 
    -The main characteristics of tuples are being ordered , heterogeneous and immutable.


'''

'''
Creating a Tuple:
1.
A tuple is created by placing all the items inside parentheses (), separated by commas.
A tuple can have any number of items and they can be of different data types.
'
2.
Using the [,] and give more then one value to a single variable 

3.
Using the tuple()  constructor.

'''

#1.Using the (ele,ele,.....)

tpl=(1,2,3,5)
print(tpl,type(tpl))

print('-------------------------------')

#Using the ele,ele,

tpl=1,2,3,4
print(tpl,type(tpl))

print('-------------------------------')

# using the tuple(iterable) constructor itrable->list,set,string ,tuple etc,

tpl=tuple("Hello")
print(tpl,type(tpl))
print('-------------------------------')

tpl=tuple([1,2,3,4,5,6])
print(tpl,type(tpl))
print('-------------------------------')


tpl=tuple({1,2,3,4,5,6,7})
print(tpl,type(tpl))
print('-------------------------------')



'''
Way to access the value of the tuple.
    1.Using indexing
    2.Using loop
    3.Using Slicing

'''
print('-------------------------------')

#creation a tuple of 10 numbers

tpl=tuple([*range(1,11)])


#1 using positive indexing
print("Value at the index 0:",tpl[0])
print("Value at the index 1:",tpl[1])
print("Value at the index 9:",tpl[9])

print('-----------------------------')


#1 using negative indexing
print("Value at the index -1:",tpl[-1])
print("Value at the index -5:",tpl[-5])
print("Value at the index -10:",tpl[-10])

print('-----------------------------')


#Using loop
print("Using Loop:")
for value in tpl:
    print(value,end=" ")

print()
print('-----------------------------')
#using slicing

print("Sliceing [:]",tpl[:])
print("Sliceing [1:4]",tpl[1:4])
print("Sliceing [1:9:2]",tpl[1:9:2])
print("Sliceing [::-1]",tpl[::-1])
print("Sliceing [:-8:-1]",tpl[:-8:-1])
print("Sliceing [:-4:-1]",tpl[:-4:-1])



print('-----------------------------')
#concatenation in tuple [+]

tup=(1,2,3,4,5)+(1000,)
print("After Concate:",tup)


print('-----------------------------')
#a mutiple type tuple 

tup=(1,[1,2,3],{"name":"jack","age":"22"},3+5j,"Hello")
tup=tup+(10,20,30)
print(tup)