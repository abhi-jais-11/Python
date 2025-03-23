class Employee:  
    def __init__(self, num1, num2): 
        self.num1=num1  
        self.num2=num2  
    def display(self): 
        print("Data of Employee")  
    def calculation(self):  
        print(f"{self.num1+self.num2}") 
        
         
class hr(Employee):  
    def __init__(self, num1, num2): 
        super().__init__(num1, num2) 
    def display(self):  
        print("Data of HR refenced by Employee")  
    def calculation(self): 
            print(f"Subtraction is {self.num1-self.num2}")  
            
            
class admin(Employee):  
    def _init_(self, num1, num2):  
        super().__init__(num1, num2)  
    def display(self):  
        print("Data of Admin refenced by Employee")  
    def calculation(self,num1,num2):  
        print(f"Multiplication is {self.num1*self.num2}") 

        
num1=int(input("enter the number")) 
num2=int(input("Enter the number"))  
object1=Employee(num1,num2)
object1.display()

object2=hr(num1,num2)
object2.display()
object2.calculation()