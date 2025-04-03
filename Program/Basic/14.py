#function to find the reverse of string using recursion

def reverse_string(str):
    if str==" " or str=="":
        return ""  
    return str[-1] + reverse_string(str[:-1])


#function call 
str="Hello"
ans=reverse_string(str)
print(f"Reverse of {str} is : {ans}")


