from abc import *

class Parent(ABC):
    @abstractmethod
    def info(self):
        pass

class Child(Parent):
    def __init__(self, *args, **kwargs):
        self.data=kwargs
        
    def info(self): 
        for key,value in self.data.items():
            print(f"{key.capitalize()}:{value}")


# obj=Child(name="Jenna Ortega",age=23,work="Model")
# obj.info()
        
        
print(globals()['Child'])