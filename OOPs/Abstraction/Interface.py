'''
1.Interface:
    - If a class contains only abstractmethods then .
    - It is called as interface .
    - It is just theoretical concept.
'''


#simple example 

from abc import *

class Db_Connection_Interface(ABC):
    '''
    If a abstract class contains only abtract method called interface.   
    '''
    
    @abstractmethod
    def create_connect(self):
        pass
    
    @abstractmethod
    def use_connect(self):
        pass
    
    @abstractmethod
    def close_connect(self):
        pass
    


class Oracle(Db_Connection_Interface):
     
    def create_connect(self):
        print(f"Create Connection With Oracle Successfully !")
    
    def use_connect(self):
        print(f"Use Connection With Oracle Successfully !")
    
    def close_connect(self):
        print(f"Close Connection With Oracle Successfully !")
        
        

class Mysql(Db_Connection_Interface):
        
        def create_connect(self):
            print(f"Create Connection With Mysql Successfully !")
        
        def use_connect(self):
            print(f"Use Connection With Mysql Successfully !")
        
        def close_connect(self):
            print(f"Close Connection  With Mysql Successfully !")



#taking the user 
db = input("Enter the Database Name : ")
class_name= globals()[db]
obj = class_name()
obj.create_connect()
obj.use_connect()
obj.close_connect()





    
    

