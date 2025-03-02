'''
Program to Remove Duplicate Word From the String.

'''

def remove_duplicate(str):
    return " ".join(set(str.split(" ")))


str=input("Enter The Srring To Remove The Duplicate Word: ")
print(f"After The Remove The Duplicate String Is:{remove_duplicate(str)}")