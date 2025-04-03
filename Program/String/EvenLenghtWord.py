
'''

Program to print the Even legnth words .

'''

def even_legnth(str):
    str=str.split(" ")
    return list(filter(lambda i : len(i)%2==0,str))


str=input("Enter The String To Print The Evel Legnth Word:")
print("Even Length Words Are:",*even_legnth(str))