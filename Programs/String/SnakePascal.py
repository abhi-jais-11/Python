
'''
Program To convert Snake case into Pascal case.

'''

def snake_pascal(str):
    
    return str.title().replace("_","")
    
    
str=input("Enter The Sting To Convert Snake Case To Pascal Case:")
print(f"Pascal Case Of The String Is :{snake_pascal(str)}")