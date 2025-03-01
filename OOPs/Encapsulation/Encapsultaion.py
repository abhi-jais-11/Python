'''
Encapsulation in Python

    -In Python, encapsulation refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class.
    -It also restricts direct access to some components, which helps protect the integrity of the data and ensures proper usage.
This approach:
    -Provides better control over data.
    -Prevents accidental modification of data.
    -Promotes modular programming.

Python achieves encapsulation through public, protected and private attributes.

How Encapsulation Works :
    -Data Hiding: 
        The variables (attributes) are kept private or protected, meaning they are not accessible directly from outside the class. Instead, they can only be accessed or modified through the methods.
    -Access through Methods: 
        Methods act as the interface through which external code interacts with the data stored in the variables. 
        For instance, getters and setters are common methods used to retrieve and update the value of a private variable.
    -Control and Security: 
        By encapsulating the variables and only allowing their manipulation via methods, the class can enforce rules on how the variables are accessed or modified, thus maintaining control and security over the data.

'''


class Encapsulation:
    
    #can access only inside the class
    __aadharNumber="53251736XXXX"

    def __init__(self):
        print("Your Aadhar Number is :",self. __aadharNumber)


encapsulation=Encapsulation()
# print(encapsulation.__aadharNumber) AttributeError: 'Encapsulation' object has no attribute '__aadharNumber'


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self._account_type = "Savings"       # Protected attribute
        self.__balance = balance             # Private attribute

    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def get_balance(self):
        """Public method to access private attribute"""
        return self.__balance

# Creating an object of BankAccount
account = BankAccount("Alice", 1000)

# Accessing public attribute
print(account.account_holder)  # Alice

# Accessing protected attribute (not recommended)
print(account._account_type)  # Savings

# Accessing private attribute directly (This will cause an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Correct way to access private data
print(account.get_balance())  # 1000

# Depositing money
account.deposit(500)
print(account.get_balance())  # 1500

        

    