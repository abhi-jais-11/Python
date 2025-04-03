#function to check string is palindrom or not 

def is_plindrome_str(str):
    return str[::-1]

#function call
str='aabbbaa'
ans=is_plindrome_str(str)
if str==ans:
    print(f"{str} is Palindrome:")
else:
    print(f"{str} is not Palindrome:")