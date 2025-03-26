'''
Method of the set:
    1.remove()
    2.pop()
    3.discard()
    4.clear()
'''

#sets of 50 nums

sets=set([*range(2,51,2)])
print(sets)

print('-----------------------------------------------------------')

'''
#1.remove(item)
Remove an element from a set; it must be a member.
If the element is not a member, raise a KeyError.
'''


sets.remove(8)
sets.remove(10)
sets.remove(12)
# sets.remove(3)   KeyError: 3

print(sets)
print('------------------------------------------------------------')



'''
2.pop()
It's remove the first element of the sets and return the element.

'''
print(sets.pop())
print(sets.pop())
print(sets.pop())
print(sets.pop())
print(sets.pop())

print(sets)
print('----------------------------------------------')


'''

3.discard(element: int, /) -> None
Remove an element from a set if it is a member.
Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.

'''

sets.discard(18)
sets.discard(19)
sets.discard(20)
sets.discard(40)
sets.discard(42)
sets.discard(44)


print(sets)
print('-------------------------------------------------')

#clear removes all element from the sets
sets.clear()
print(sets)