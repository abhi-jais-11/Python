'''
reverse(): Reverses the order of the elements in the list.
sort(): Sorts the list in ascending order (by default).
index(): Returns the index of the first occurrence of a specified element.
count(): Returns the number of times a specified element appears in the list.
len():Return the length of the list.

'''

#reverse()

lst=[1,2,3,4,5,2,3,3,3,3,3,3]
lst.reverse()
print(lst)

name=['a','b','s','d']
name.reverse()
print(name)

print('------------------------------------------------------')

'''
Syntax of sort() method
list_name.sort(key=None, reverse=False)

Parameter:

key (Optional): This is an optional parameter that allows we to specify a function to be used for sorting. For example, we can use the len() function to sort a list of strings based on their length.
reverse (Optional): This is an optional Boolean parameter. By default, it is set to False to sort in ascending order. If we set reverse=True, the list will be sorted in descending order.
Return:


'''
name.sort(reverse=True)
print(name)

a = ["apple", "banana", "kiwi", "cherry"]

a.sort(key=len)
print(a)

print('--------------------------------------------------')

'''
Syntax of List index() Method
Syntax: list_name.index(element, start, end) 

Parameters: 


element: The element whose lowest index will be returned.
start(optional): The position from where the search begins.
end(optional): The position from where the search ends.
'''

print(lst.index(3,0,4))

print('--------------------------------------------------')
#len([....])
print(len(lst))

print('--------------------------------------------------')
print(lst.count(5))





'''
1.max()->return max from the iterator of numbers.
2.min()->return min from the iterator of numbers.
3.sum()->return sum  of numbers.
'''


#max(arg1,arg2,*args,*[key=fun])
lst=[1,2,3,4,5,100,39,200]
print(max(lst))#200

print('----------------------------------------')
#min(arg1,arg2,*args,*[key=fun])
print(min(lst))



print('--------------------------------')
#sum()
print(sum(lst))
