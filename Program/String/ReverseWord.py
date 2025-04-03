
'''
Program to reverse of the word of the string.

'''

def reverse_word(str):
    
    str=" ".join(str.split(" ")[::-1])
    return str

    
    
str=input("Enter The String To Reverse Of Word:")
print(f"Rverse Word Of the String:{reverse_word(str)}")