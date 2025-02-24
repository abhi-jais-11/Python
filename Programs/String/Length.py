'''
2.Write a program to find the length of the given string.

'''

#1. by using len() function

def str_length(str):
    return len(str)


#2. without using len()
def lenght_str(str):
    count=0
    for _ in str:
        count+=1
    return count



str=input("Enter the String:")
print(f"Length of the string is : {str_length(str)}")
print(f"Length of the string is : {lenght_str(str)}")

