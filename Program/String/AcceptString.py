
'''
Program To Accept a stirng if exist all vowel in the string.

'''

def accept_string(str):
    vowel=['a','i','o','u','e']
    
    if all(i in str.lower() for i in vowel):
        return True

    
    
    
str=input("Enter The String:")

if accept_string(str):
    print("Accepted String:")
else:
    print("Not Accepted String:")