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







'''
Protected Access Modifier:
   -The members of a class that are declared protected are only accessible within the class where it is declared and its subclass. -To implement protected field or method, the developer follows a specific convention mostly by adding prefix to the variable or function name. 
   -Popularly, a single underscore “_” is used to describe a protected data member or method of the class.
   -Note that the python interpreter does not treat it as protected data like other languages, it is only denoted for the programmers since they would be trying to access it using plain name instead of calling it using the respective prefix. 
   For example,
   -It is convension that it can access outside of the class.

'''


'''
Private Access Modifier:
    -The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier.
    -Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class. 


'''