'''
1.Case change in  the string.

'''
str="Hii,I'm Abhinav Jaiswal"

print('---------------------case change------------------------------')
# uppercase ->str.upper()

print(str.upper())

# lowercase->str.lower()

print(str.lower())

#title case ->str.title()

print(str.title())


# swapcase -> str.swapcase()  it cnage opposite of the currentcase of each charector

print(str.swapcase())


# capitalize -> str.capitalize()

print(str.capitalize())



str="This is a string."

'''
1. find(“string”, beg, end) :- This function is used to find the position of the substring within a string.
    -It takes 3 arguments, substring , starting index( by default 0) and ending index( by default string length). 
    -It returns “-1 ” if string is not found in given range.
    -It returns first occurrence of string if found.
    
2.rfind(“string”, beg, end) :- This function has the similar working as find(), but it returns the position of the last occurrence of string.
'''

print('--------------------find the index of substring --------------------------')
print(str.find('is',0,10))
print(str.find('a'))
print(str.find('j'))
print(str.rfind('is'))
print(str.rfind('s'))
'''
3. startswith(“string”, beg, end) :- The purpose of this function is to return true if the function begins with mentioned string(prefix) else return false.
4. endswith(“string”, beg, end) :- The purpose of this function is to return true if the function ends with mentioned string(suffix) else return false.

'''
print('-------------------check the string start and end with------------------------')
print(str.startswith('This',0,10))
print(str.endswith('n'))

'''
5. islower(“string”) :- This function returns true if all the letters in the string are lower cased, otherwise false.
6. isupper(“string”) :- This function returns true if all the letters in the string are upper cased, otherwise false.

'''
print('-------------------check the isupper or islower------------------------')
print(str.isupper())
print(str.islower())

