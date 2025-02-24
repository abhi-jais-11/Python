'''
1.Write a program to check the given string is palindrom or not?

    if a string read same forword and backword the it will a palindrom string:
        ex:
            aba=aba -> palindrom
            abb=bba -> not palindrom


'''

def is_palindrome(str):
    return str[::-1]


str=input("Enter the String:")

if str==is_palindrome(str):
    print(f"String {str} is Palindrom:")
else:
    print(f"String {str} is not Palindrom:")
    
