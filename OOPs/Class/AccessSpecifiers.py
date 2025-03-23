'''
Access Specifiers.
    -Python does not have such keywords since it is a scripting language, and it is interpreted instead of being compiled. 
    -Mainly, Access Modifiers can be categorized as Public, Protected and Private in a class.

'''


'''
Public Access Modifier:
    -The members of a class that are declared public are easily accessible from any part of the program.
    -All data members and member functions of a class are public by default. 
'''

class Public:
    
    #public
    college_name="BIET"
    
    def __init__(self,name,age):
        
        #public 
        self.name=name
        self.age=age
    
    def get_info(self):
        print("-----------------Public Access Sepecifiers--------------------------")
        print(f"Name:{self.name}\nAge:{self.age}\nCollege:{self.college_name}")
        
        
    
        
    

public=Public("Abhi",22)
public.get_info()

'''
Protected Access Modifier:
   -The members of a class that are declared protected are only accessible within the class where it is declared and its subclass. -To implement protected field or method, the developer follows a specific convention mostly by adding prefix to the variable or function name. 
   -Popularly, a single underscore “_” is used to describe a protected data member or method of the class.
   -Note that the python interpreter does not treat it as protected data like other languages, it is only denoted for the programmers since they would be trying to access it using plain name instead of calling it using the respective prefix. 
   For example,
   -It is convension that it can access outside of the class.

'''


class Protected:
    
    #public
    _name=None
    _age=None
    _college=None
    
    def __init__(self,name,age,college):
        
        #public 
        self._name=name
        self._age=age
        self._college=college
    
    def get_info(self):
        print("-----------------Protected Access Sepecifiers--------------------------")
        print(f"Name:{self._name}\nAge:{self._age}\nCollege:{self._college}")
        
        
    
        
    

protect=Protected("Abhi",22,"BIET")
protect.get_info()

# protect(protect._name) #TypeError: 'Protected' object is not callable [can access inside the class and subclass]



'''
Private Access Modifier:
    -The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier.
    -Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class. 



'''
class Private:
    
    #public
    __name=None
    __age=None
    __college=None
    
    def __init__(self,name,age,college):
        
        #public 
        self.__name=name
        self.__age=age
        self.__college=college
    
    def get_info(self):
        print("-----------------Private Access Sepecifiers--------------------------")
        print(f"Name:{self.__name}\nAge:{self.__age}\nCollege:{self.__college}")

private=Private("Abhi",22,"BIET")
private.get_info()
# print(private.__name)AttributeError: 'Private' object has no attribute '__name'

#we can use this to access 
