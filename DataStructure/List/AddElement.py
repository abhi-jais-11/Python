'''
Adding Elements into List
We can add elements to a list using the following methods:
    -append(): Adds an element at the end of the list.
    -extend(): Adds multiple elements to the end of the list.
    -insert(): Adds an element at a specific position.

'''


lst=[]

#append(item)
lst.append(10)
lst.append(20)
print(lst)

#extend([item,item2,item...])
lst.extend([1,2,3,4,5,6,7,8,9])
print(lst)


#inset(index,item)
lst.insert(2,100)
print(lst)



# update the element of the list

lst[0]=1000
print(lst)


'''
Slicing of the list

'''
print(lst[::])
print(lst[1:5])
print(lst[::-1])
print(lst[1:8:2])
print(lst[-8:])