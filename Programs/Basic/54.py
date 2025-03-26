# Write a program to count the frequency of each word in a string using a dictionary
def frequency_count(str):
    str=str.split()
    dct={}
    count=1
    for i in str:
        if i in dct:
            dct[i]=count+1
        else:
            dct[i]=count
    return dct
        
      

# driver code
str = "The curious fox leapt gracefully over the moonlit stream, chasing shadows in the quiet forest. The curious fox leapt gracefully."

f_count = frequency_count(str)

print(f"Frequency of ech word is : {f_count}")
