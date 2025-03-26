'''
Python Sets
    -Python set is an unordered collection of multiple items having different datatypes. 
    -In Python, sets are mutable, unindexed and do not contain duplicates. 
    -The order of elements in a set is not preserved and can change.


Way to create:
    1.Using {ele,...} if we not add the value it treat as a empty dictionary.
    2.Using set() constructor.
'''

#1.using {ele....}

# #without element
# sets={}
# print(type(sets),sets) #<class 'dict'> {}
# print('--------------------------')

#with value
sets={1,2,3}
print(type(sets),sets)  #<class 'set'> {1, 2, 3}
print('--------------------------')


#for creating the empty set you can use the set()
#set=()
# print(type(sets),sets)

sets=set([1,2,3,4,5,6,7,8,8,9,9,10])

'''
Way to access the value of the set.
    1.Using loops. 
'''
# print(sets[0]) #TypeError: 'set' object is not subscriptable

for items in sets:
    print(items,end=" ")
    
print()
print('--------------------------')



'''
Way to add the element in sets:
    1.add(element)
    2.update(Iterable)

'''

'''
1.add(element)
Add an element to a set.
This has no effect if the element is already present.

'''

sets=set()

sets.add(10)
sets.add(20)
sets.add(10)
# sets.add(40,40) #TypeErro only one element at a time 
print(sets)


print('-------------------------------------')


'''
2.update(Iterable) 
It can add more then one value at a time .
it use the  Iterable to add the element.

'''
sets=set()
sets.update([*range(2,21,2)])
print(sets)
