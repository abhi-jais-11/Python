#Write a program to check if two strings are anagrams of each other.

def is_anagram(str1,str2):
    
    return sorted(str1.lower())==sorted(str(str2).lower())


#driver code 

str_1="Silent"
str_2="Listen"

is_angrm=is_anagram(str_1,str_2)

if is_angrm:
    print(f"String Is Anagram :")
else:
    print(f"String is Not Anagram :")