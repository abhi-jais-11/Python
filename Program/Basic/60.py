#Write a program to find the first non-repeating character in a string.

def non_reapeating(str):
    lst=[i for i in str]
    str=" "
    for i in lst:
        if lst.count(i) > 1:
            pass
        else:
            str+=i
    return str

#driver code 
str="program to find the first non repeating character in a string"
non_repeat_char=non_reapeating(str)
print(f"Non Repeating Char are: {non_repeat_char} ")
