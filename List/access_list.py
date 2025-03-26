'''
Access :
    -Extract the element from the list.
    
Way to access list element :
    1.Using Index
    2.Using Loop
    3.slicing
'''

#
lst=["Jack","Anna","Alexa","Maria","Xie"] 

#using positive indexing
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])
print('--------------------')
#using negative indexing
print(lst[-1])
print(lst[-2])
print(lst[-3])
print(lst[-4])
print(lst[-5])

print('--------------------')
#using loop

for item in lst:
    print(item)
    
print('--------------------')
#using slicing list_name[start default=0:end:step default=1] retrun list
print(lst[:1]) 
print(lst[1:2])
print(lst[2:3])
print(lst[3:4])
print(lst[4:5])

print('--------------------')
#printing using step
print(lst[0:5:2])

print('--------------------')
#reverse using slicing
print(lst[::-1])
