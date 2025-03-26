'''
Removing Elements from List
We can remove elements from a list using:
    -remove(): Removes the first occurrence of an element.
    -pop(): Removes the element at a specific index or the last element if no index is specified.
    -del statement: Deletes an element at a specified index.
    -clear():Remove all element from the list.

'''
lst=[*range(1,21)]
print(lst)
print('------------------------------------------')



# -remove(): Removes the first occurrence of an element. Raise Value Error If not present.
lst.remove(10)
lst.remove(20)
lst.remove(5)
lst.remove(11)
lst.remove(19)
print(lst)
# print(lst)
# lst.remove(21) #ValueError: list.remove(x): x not in list
print('------------------------------------------')




#-pop(): Removes the element at a specific index or the last element if no index is specified.
#and return the remove element [default index is -1]

print(lst.pop())
print(lst.pop())
print(lst.pop())
print(lst.pop())
print(lst)



#del statement: Deletes an element at a specified index.
print('----------------------------------------')
del lst[0]
del lst[6]
del lst[4]
del lst[4]
print(lst)



print('----------------------------------------')
#clear():Remove all element from the list.

lst.clear()
print(lst)