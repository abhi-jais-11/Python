
'''

1.write a program to reverse words.
    Hii Hello  -> Hello Hii
    
'''

def reverse_word(str):
    str=str.split(" ")
    return   str[::-1] 
    
str=input("Enter the String:")
print("Reverse Word Is:",*reverse_word(str))

