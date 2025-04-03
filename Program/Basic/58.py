#Write a program to find the longestword word in a string.

def long_word(str):
    str=str.split()
    return max(str,key=len)


#driver code
str="A program to find the longestword word in a string."
long_word=long_word(str)
print(f"Longest Word is : {long_word} ")
