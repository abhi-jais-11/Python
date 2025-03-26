'''
Private Access Modifier:
    -The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier.
    -Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class.
    -We can also access outside of the class using the special syntax [objname._classname__method/varibalename]
    -But it's not recommende to access outside of the class.
     

'''


#simple example

class Private:
    
    __privateVariable="Private Varibale"
    
    
    def __init__(self, *args, **kwargs):
        self.__privateMethod()
    
    
    def get_Private(self):
        print("Isside the Public Metho:")
        print(self.__privateVariable)
    
    def __privateMethod(self):
        print("Isside the Private Method:")
        print(self.__privateVariable)
    
    


#object 
prv_obj=Private()
print('------------------')
prv_obj.get_Private()

print('-------------------')
print('Outside the class using special syntax:')
prv_obj._Private__privateMethod()


'''
Note: 
    -Python does not support the strict encapsulation [and there are no concept of strinct public, private,and protected],
    -Thst's Why it's not 100% oops. 
'''