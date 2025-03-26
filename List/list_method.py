'''
reverse(): Reverses the order of the elements in the list.
sort(): Sorts the list in ascending order (by default).
index(): Returns the index of the first occurrence of a specified element.
count(): Returns the number of times a specified element appears in the list.
len():Return the length of the list.

'''
from random import randint

#reverse()
lst=[*range(1,5)]
lst.reverse()
print(lst)


print('------------------------------------------------------')
name_lst=["Abhinav","Zue","John"]
name_lst.reverse()
print(name_lst)






print('------------------------------------------------------')

'''
Syntax of sort() method
list_name.sort(key=None, reverse=False)

Parameter:

key (Optional): This is an optional parameter that allows we to specify a function to be used for sorting. For example, we can use the len() function to sort a list of strings based on their length.
reverse (Optional): This is an optional Boolean parameter. By default, it is set to False to sort in ascending order. If we set reverse=True, the list will be sorted in descending order.
Return:


'''
lst=[]
for i in range(1,6):
    lst.append(randint(1,1000))
print(lst)

print('--------------------------------------------------')
lst.sort()
print(lst)

print('--------------------------------------------------')
lst.sort(reverse=True)
print(lst)


print('--------------------------------------------------')
name_lst=["Abhinav","Zue","John"]
name_lst.sort(key=len,reverse=True)
print(name_lst)

print('--------------------------------------------------')







print('-----------------------------------')
'''
Syntax of List index() Method
Syntax: list_name.index(element, start, end) 

Parameters: 

element: The element whose lowest index will be returned.
start(optional): The position from where the search begins.
end(optional): The position from where the search ends.
'''

lst=[*range(1,11)]
index=lst.index(10)
print(f"Index of the element {10} is:",index)



print('--------------------------------------------------')

print(f"Index of the element {4} is {lst.index(4,0,6)} search in 0-6")






print('--------------------------------------------------')
#
print("Legnth of the list is:",len(lst))



print('--------------------------------------------------')
#
print(f"count the occurence of the {4} is list {lst.count(4)}")
print(f"count the occurence of the {1} is list {lst.count(1)}")




print('--------------------------------------------------')



'''
1.max()->return max from the iterator of numbers.
2.min()->return min from the iterator of numbers.
3.sum()->return sum  of numbers.
'''


#max(arg1,arg2,*args,*[key=fun])

print(f"Max Value In list : {name_lst} is According to Length : ",max(name_lst,key=len))
print('---------------------------------------------------------------------------')
print(f"Max Value In list : {name_lst} is Without Length : ",max(name_lst))

print('----------------------------------------------------------------')
print(f"max value In list {lst} is : ",max(lst))








print('----------------------------------------------------------------')
#min(arg1,arg2,*args,*[key=fun])

print(f"Min Value In list : {name_lst} is According to Length : ",min(name_lst,key=len))
print('----------------------------------------------------------------')
print(f"Min Value In list : {name_lst} is Without Length : ",min(name_lst))
print('-------------------------------------------------------------')
print(f"min value In list {lst} is : ",min(lst))


print('----------------------------------------------------------------')

print("Sum of the list is :",sum(lst))

print("Sum of the list is Adding 15 using start in sum() :",sum(lst,start=15))