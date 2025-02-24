'''
Removing Elements from List
We can remove elements from a list using:
    -remove(): Removes the first occurrence of an element.
    -pop(): Removes the element at a specific index or the last element if no index is specified.
    -del statement: Deletes an element at a specified index.
    -clear():Remove all element from the list.

'''

#remove(item)

lst=[1,2,3,4,5,6,7,8,9,9,17]
print(lst)
print('----------------------------------')
lst.remove(7)
lst.remove(17)
print(lst)


#pop(item) and return element
print('----------------------------------')
lst.pop()#last element
lst.pop(2)
print(lst)


#del lst[index]
print('----------------------------------')
del lst[5]
print(lst)


#clear
print('----------------------------------')
lst.clear()
print(lst)