
class Encpasulation:
    def __init__(self,email):
        self.__email = email
    def __display(self):
       print("Email is : ",self.__email)
       
    def display(self):
        self.__display()
    
    

obj = Encpasulation("Abhi12@gmail.com")
obj.display()
# print(obj.__email) # This will throw an error as __email is private variable
# print(obj._Encpasulation__email) # This will print the value of __email
