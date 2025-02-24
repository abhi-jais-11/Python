'''
Python Sets
    -Python set is an unordered collection of multiple items having different datatypes. 
    -In Python, sets are mutable, unindexed and do not contain duplicates. 
    -The order of elements in a set is not preserved and can change.

'''

'''
1.Creating a Set in Python
'''
set={1,2,3,4}
print(set)

# set={} give an empty dictionary

set={}
print(type(set)) # return dict 


nameSet={'Raj','Rahul','Ramesh'}
print(nameSet)
print('----------------------------')

'''
2.Adding Elements to a Set in Python
    -We can add items to a set using add() method and update() method. 
    -add() method can be used to add only a single item.
    -To add multiple items we use update() method.
'''

set={1,}
set.add(10)
set.add(20)
set.add(13)
print(set)


set.update([10,20,30,40,50,60,12,24])
print(set)
print('--------------------------------')


'''
3.Accessing a Set in Python
    We can loop through a set to access set items as set is unindexed and do not support accessing elements by indexing.
    Also we can use in keyword which is membership operator to check if an item exists in a set.

'''
for _ in set:
    print(_,end=" ")
print()

print('--------------------------------------')

'''
4.Removing Elements from the Set in Python
We can remove an element from a set in Python using several methods: remove(), discard() and pop(). Each method works slightly differently :
Using remove() Method or discard() Method
Using pop() Method
Using clear() Method

'''
'''
remove() method removes a specified element from the set.
If the element is not present in the set, it raises a KeyError.
discard() method also removes a specified element from the set. 
Unlike remove(), if the element is not found, it does not raise an error.
'''


print(set)


#remove(item)
set.remove(30)
# set.remove(300) KeyError: 300
print(set)


#discard(item)
set.discard(60)
set.discard(40)
set.discard(300)
print(set)


#pop(index default first in set and last in others)

print('-----------------------------------')
set.pop()
set.pop()
print(set)


#clear() is use to remove the all record at a time 

set.clear()
print(set)