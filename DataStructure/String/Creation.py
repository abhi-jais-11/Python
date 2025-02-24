'''
1.Cretaion of the string

'''
print('--------------------------------Accessing String----------------------------------')
str='This is the string.'
str2='''This is 
multiline string.
'''
print(str)
print(str2)


'''
2. Accesing the charector of the String using index.

'''
print(str[0])#T
print(str[2])
print(str[-2]) # negative indexing from backword to forword .



'''
3.Accessing the string using loop.

'''
print('--------------------------------Accessing String using loop----------------------------------')
for i in str:
    print(i,end=" ,")

print()
print('--------------------------------Accessing slicing----------------------------------')
'''
4.slicing the string 

str[start:end:step] [start-index,end-index,step-count-to-increse/decrease]

ex:

'''
print()
str="Hii I'm Abhinav Jaiswal."
print(str[0:5])
print(str[1::2])
print(str[::-1])

numStr='22'
print(numStr[::-1])


print('--------------------------------String Immutability----------------------------------')
'''
5.Strings in Python are immutable. 
    -This means that they cannot be changed after they are created.
    -If we need to manipulate strings then we can use methods like concatenation, slicing, or formatting to create new strings based on the original.
'''

str="hello"
# str[0]='m' #TypeError: 'str' object does not support item assignment


'''
6.Update string using the slice 

'''
str="H"+str[1:]
print(str)



print('-------------------------------Delete String----------------------------------')
del str
del str2
