#Write a program to check if a string contains all unique characters.

def find_unique_str(str):
    lst=[]
    for chr in str:
        if chr in lst:
            return False
        else:
            lst.append(chr)
    return True



#driver code 
str="abcde"
unique_str=find_unique_str(str)

if unique_str:
    print(f"All Charecters are unique")
else:
    print(f"Not all Charecters are  unique")