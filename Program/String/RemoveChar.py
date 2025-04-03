
'''
Program to remove the i'th charecter from the string

'''

def remove_char(str,i):
   return  str[:i]+str[i+1:]

    
    
str=input("Enter The String :")
i=int(input("Enter The Position To Remove The String Char:"))

print(f"String After Remove The Char :{remove_char(str,i)}")