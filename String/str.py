'''
Python String
    -A string is a sequence of characters.
    -Python treats anything inside quotes as a string. 
    -This includes letters, numbers, and symbols. 
    -Python has no character data type so single character is a string of length 1.
    -It treate a sequence which can be access using the index .
    -It is immutable data type we can't change the value of existing charecter or words.

    Ex:
        str1='This is string.'
        str2="This is String."
        str3=""" this is multiline string  """
'''


'''
Way to create a string.
    Using quate['',"",''' ''',""""  """]
    
'''
print('----------------------------------')

#1 using quates


str='Hii,I am a string with single quate.'
print(str)

print('----------------------------------')

str="Hii,I am a string with double quate."
print(str)

print('----------------------------------')

str="""
Hii,I am a string with Triple  double quate.
And also I'm Multiline String.
"""
print(str)


print('----------------------------------')

str='''
Hii,I am a string with Triple  single quate.
And also I'm Multiline String.
'''
print(str)

print('----------------------------------')


'''
Way to access the charecter of the string.
    1.Indexing
    2.loops
    3.slicing
    
'''

#1.indexing [positive and negative]

str='Hii,I am a string you can access uaing indexing.'

#+ve
print(str[0])
print(str[1])
print(str[4])

print('-------------------------------------') 

#-ve 
print(str[-2])
print(str[-4])
print(str[-6])

print('-------------------------------------------------')

#using for loop

for char in str:
    print(char,end="")

print()
print('---------------------------------------------------')

#using slcicing

print(str[1:10])
print(str[0:5])
print(str[1:10:2])
print(str[-4:-1])
print(str[:-8:-1])
print(str[-3:-8:-1])
print(str[::-1]) #reverse string

print('-------------------------------------------------')

# str[0]="h" #TypeError: 'str' object does not support item assignment
# str[1]="b" #TypeError: 'str' object does not support item assignment

