'''
Python Lists
    -In Python, a list is a built-in dynamic sized array (automatically grows and shrinks). 
    -We can store all types of items (including another list) in a list. 
    -A list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations and actual items maybe stored at different locations.
    -List can contain duplicate items.
    -List in Python are Mutable. Hence, we can modify, replace or delete the items.
    -List are ordered. It maintain the order of elements based on how they are added.
    -Accessing items in List can be done directly using their position (index), starting from 0.

    Ex:
        lst=[]
        lst=[item1,item2,......]
'''


'''
Way to create a list:
    1.Using [] 
    2.Using list() constructor


'''

#Example.

lst=[1,2,3,4,5]
print(lst)


print('-----------------------------------------------')
#it can take only one argument
lst=list((1,2,3,4,5,6)) 
print(lst)



print('-----------------------------------------------')
lst=list([1,2,3,4,5,6])
print(lst)




print('-----------------------------------------------')
lst=list({1,2,34,56,7})
print(lst)
# lst=list(1,2,3)  #TypeError-> list expected at most 1 argument, got 3



print('-----------------------------------------------')
lst=["Jack","Anna","Alexa","Maria","Xie"] #list of string
print(lst)



print('-----------------------------------------------')
lst=[[1,2,3,4,56],["Jack","Anna","Alexa","Maria","Xie"]] #nested list
print(lst)




print('-----------------------------------------------')
lst=[1,2,3,(1,2,3,4),{1,2,3},"Jack","Anna","Alexa","Maria","Xie",2+3j] #Mixed data type list
print(lst)