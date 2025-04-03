#Write a program to count the number of uppercase and lowercase letters in a string.
def upper_lower_char_count(str):
    l_count=0
    u_count=0
    for i in str:
        if i == i.lower() :
            l_count+=1
        else:
            u_count+=1
            
    return u_count,l_count


str="Abhi Jais"

u_count,l_count=upper_lower_char_count(str)

print(f"Upper count: {u_count} and Lower count : {l_count}")
