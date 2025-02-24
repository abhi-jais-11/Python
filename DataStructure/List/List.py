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
1.cretion of list
    Using Square Brackets
    Using List contructor

'''
# List of integers
number_lst=[1,2,3,4,5]

# List of strings
string_list=['jack','mice','john']


#list of mixed
mixed_list=[1,1.5,10,'jack',1+3j]

print(number_lst)
print(string_list)
print(mixed_list)


# list constructor
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

#repeate the number of the list
print(number_lst*2)
print('---------------------------------------------')



'''
2. Accessing the element of the list.
    1.using individual index
    2.using loop
    
'''

print(number_lst[0])
print(number_lst[2])

for i in number_lst:
    print(i,end="->")
print()
print('---------------------------------------------')


#nested list

lst=[
    [1,2],
    [2,3],
    [4,5] ]
print(lst[0][1])