from str_module import is_str_plindrome

str=input("Enter String to Check Palindrome:")

is_palindrome=is_str_plindrome(str)

if is_palindrome:
    print(f"{str} is Plindrome:")
else:
     print(f"{str} is not Plindrome:")