'''
1.Program to check the given string is palindrom or not .

'''

def is_palindrom(str):
    
    #reverse of string 
    return str[::-1]


str=input("Enter The String To Check Is Plindrom Or Not:")

if str==is_palindrom(str):
    print(f"{str} Is Palindrom !")
else:
    print(f"{str} Is Not Plindrom !")
    