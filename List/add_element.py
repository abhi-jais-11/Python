'''
Adding Elements into List
We can add elements to a list using the following methods:
    -append(): Adds an element at the end of the list.
    -extend(): Adds multiple elements to the end of the list.
    -insert(): Adds an element at a specific position.

'''



#append(element) it can take only one argument or element
lst=[]
lst.append(1) 
lst.append(2)
lst.append(3) 
lst.append(4)
print(lst)



print('--------------------------------')
#using loop and append()
lst=[]
for i in range(1,11):
    lst.append(i)

print(lst)


print('--------------------------------')
#extend(iterable): Adds multiple elements to the end of the list. 

lst=[]
lst.extend({1,2,3,4,5,6,7})
print(lst)



print('--------------------------------')
lst=[]
lst.extend([1,2,3,4,5,6,7])
print(lst)



print('--------------------------------')
lst=[]
lst.extend((1,2,3,4,5,6,7))
print(lst)

# lst=[]
# lst.extend(1,2,3,4,5,6,7) #TypeError: list.extend() takes exactly one argument (7 given)
# print(lst)


print('--------------------------------')
#insert(): Adds an element at a specific position.
lst=[]
for i in range(1,6):
    lst.append(i)

print(lst)



print('--------------------------------')
#insert(): Adds an element at a specific position. and sift the element 
lst.insert(1,8)
lst.insert(4,10)
lst.insert(2,99)
lst.insert(3,100)
print(lst)

