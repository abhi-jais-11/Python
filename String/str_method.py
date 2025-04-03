'''
String Methods:

    1.upper()
    2.lower()
    3.capitalize()
    4.titile()
    5.swapcase()
    6.find()
    7.rfind()
    8.startwith()
    9.endswith()
    10.isupper()
    11.islower()
    12.replace()
    13.strip()
    14.rstrip()
    15.lstrip()


'''

str="Hello, Jack ! Are you 22 Year Old."


#1.upper() Convert the string into uppercase.

print("Upper Case: {}".format(str.upper()))

print('--------------------------------------------------------------')

#2.lower() Convert the string into lowercase.

print("Lower Case: {}".format(str.lower()))


print('--------------------------------------------------------------')

#3.capitalize() Convert the string into capitalize.

print("Capitalize Case: {}".format(str.capitalize()))


print('--------------------------------------------------------------')

#4.title() Convert the string into title.

print("Title Case: {}".format(str.title()))

print('--------------------------------------------------------------')

#5.swapcase() Convert the string into swapcase.

print("Swapcase Case: {}".format(str.swapcase()))



'''
6.find(“string”, beg, end) :- This function is used to find the position of the substring within a string.
    -It takes 3 arguments, substring , starting index( by default 0) and ending index( by default string length). 
    -It returns “-1 ” if string is not found in given range.
    -It returns first occurrence of string if found.
'''
print('--------------------------------------------------------------')

print("The char/substring {} present at the index {} in string.".format('Jack',str.lower().find("Jack".lower(),0,)))

print('--------------------------------------------------------------')

'''
7.rfind(“string”, beg, end) :-
This function has the similar working as find(), but it returns the position of the last occurrence of string.

'''

print('--------------------------------------------------------------')

print("The char/substring {} present at the index {} in string.".format('Jack',str.lower().rfind("Year".lower())))

print('--------------------------------------------------------------')


#8.startswith(str,start,end) #return True or False

print("The String startswhith {} or not : {}".format("h",str.lower().startswith("h".lower())))

print('-------------------------------------------')

#9.endswith(str,start,end) #return True or False

print("The String endswhith {} or not : {}".format("d",str.lower().startswith("d".lower())))

print('-------------------------------------------')


#10.isupper() #return True or False

print("String is in uppercase or not :{}".format(str.isupper()))

print('------------------------------------------------------')


#11.islower() #return True or False

print("String is in lowercase or not :{}".format(str.islower()))

print('------------------------------------------------------')

#12.replace(old,newvalue)

print("Replace {} in string with : {} ".format('22',str.replace('22','23')))


print('------------------------------------------------------')

str="          Hello           "

#13.strip() #remove space from both side of the string.

print("Removing the Space both side of  string : {} ".format(str.strip()))

print('---------------------------------------------------------')

#14.rstrip() #remove space from left side of the string.

print("Removing the Space right side of  string : {} ".format(str.rstrip()))

print('---------------------------------------------------------')

#15.lstrip() #remove space from left side of the string.

print("Removing the Space left side of  string : {} ".format(str.lstrip()))

print('---------------------------------------------------------')


str="Hello, Jack ! Are you 22 Year Old."


'''
16.isalpha()


Return True if the string is an alphabetic string, False otherwise.
A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.



'''
print(str.isalpha())

