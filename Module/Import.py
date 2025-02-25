'''
There are the way to import 

1.import module
2.import module as <module name you want>
3.from module  import * #each and everythings from the module
4.from module import <specific function>

'''

#accessing using Module
import Module 

print("Sum of the numbers is:",Module.add(10,20))
print("Sub of the numbers is:",Module.sub(10,20))
print("Mul of the numbers is:",Module.mul(10,20))
print("Div of the numbers is:",Module.div(20,10))
print("Mod of the numbers is:",Module.mod(10,2))
print("Power of the numbers is:",Module.powd(10,2))

print('-----------------------------------------------')



#accessing using change modulename
import Module as mod
print("Sum of the numbers is:",mod.add(10,20))
print("Sub of the numbers is:",mod.sub(10,20))
print("Mul of the numbers is:",mod.mul(10,20))
print("Div of the numbers is:",mod.div(20,10))
print("Mod of the numbers is:",mod.mod(10,2))
print("Power of the numbers is:",mod.powd(10,2))

print('-----------------------------------------')
from Module import *
print("Sum of the numbers is:",add(10,20))
print("Sub of the numbers is:",sub(10,20))
print("Mul of the numbers is:",mul(10,20))
print("Div of the numbers is:",div(20,10))
print("Mod of the numbers is:",mod(10,2))
print("Power of the numbers is:",powd(10,2))

print('--------------------------------------------')

from Module import add
print("Sum of the numbers is:",add(10,20))


