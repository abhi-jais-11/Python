# if a abstract class contains only the abstract method then we can call that class as fully abstract class. 
# Or interface class.
#Ex.

from abc import ABC,abstractmethod
class Fruit(ABC): #abstract class
    @abstractmethod
    def taste(self): #abtract method
        pass

class Mango(Fruit): #child must be override the method of parent class then it'll valid.[not use pass]
     def taste(self):
         print("Sweet")
m=Mango()
m.taste()
