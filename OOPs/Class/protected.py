'''
Protected Access Modifier:
   -The members of a class that are declared protected are only accessible within the class  and its subclass. 
   -We can also access outside of the class directly [ It is convension in python ].
   -Popularly, a single underscore “_” is used to describe a protected data member or method of the class.
   -Note that the python interpreter does not treat it as protected data like other languages, it is only denoted for the programmers since they would be trying to access it using plain name instead of calling it using the respective prefix. 
   For example,

'''
class Protected:
    
    #protected variables 
    _college_name="BIET"
    _college_add="Lucknow"
    
    #special method called constructor in python
    def __init__(self,name,age):
        self._name=name
        self._age=age
    
    
    #protected methods
    def _get_info(self):
        print(f"Name:{self._name}\nAge:{self._age}\nCollege:{Protected._college_name}\nCollegAdd:{Protected._college_add}")
        
    
    def set_info(self,name,age,colleg_name,colleg_add):
        Protected._college_name=colleg_name
        Protected._college_add=colleg_add
        self.__init__(name,age)#calling constuctor
        print("Protected Method Inside of The class:")
        self._get_info() #calling info protected method 
        


#object  creation

pub_obj=Protected("Jack",22)
pub_obj.set_info("JackSone",23,"DDU","Delhi")


#convension
print('------------------------------------')
print("Protected Method Outside of The class:")
pub_obj._get_info()



class SubClass(Protected):
    
    def __init__(self, name,age):
        super().__init__(name,age)
    
    
    def get_info(self):
        print("Protected Method Inside of The class:")
        super()._get_info()
    
    def subset_info(self,name,age,colleg_name,colleg_add):
        Protected._college_name=colleg_name
        Protected._college_add=colleg_add
        super(Protected, self).__init__(name,age)




#object creation
print('------------------------------')
print('Using The Subclass Of the Class:')
sub_obj=SubClass("Anney",22)
sub_obj.get_info()
pub_obj.set_info("Anney",23,"DU","Delhi")
print('------------------------------')
sub_obj.get_info()