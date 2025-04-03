from str_module import is_anagram

str1=input("Enter First String :")
str2=input("Enter Second String :")

is_angm=is_anagram(str1,str2)

if is_angm:
    print(f"String is Anagrams:")
else:
    print(f"String is not Anagrams")

print(globals())