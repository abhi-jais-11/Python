'''
Self in Python class?
    -Self represents the current instance of the class. 
    -By using the “self”  we can access the attributes and methods of the class in Python. 
    -When working with classes in Python, the term “self” refers to the instance of the class that is currently being used.
    -It is customary to use “self” as the first parameter in instance methods of a class.
    -Whenever you call a method of an object created from a class, the object is automatically passed as the first argument using the “self” parameter. 
    -This enables you to modify the object’s properties and execute tasks unique to that particular instance.

'''

#siple example of the self we can write class and method name same in the python it will not give any error.


class Self:
    def Self(self,greet):
        self.greet=greet
        print(self.greet)
        
        
#calling the method using the object

self_obj=Self()
self_obj.Self("Hello Welcome To The Self.")


''' 
        
Is self in Python a Keyword?
    No, ‘ self ‘ is not a keyword in Python. 
    Self is just a parameter name used in instance methods to refer to the instance itself.
        
'''

#if we are not using self inside the metod then the first argumets of the method treate as self
# we can write any name at the place of the self but recomnded self 


class Args_Self:
    def args_self(name,user_name):
        name.name=user_name
        print(name.name)
        

args_obj=Args_Self()
args_obj.args_self("Hii, I'm Abhi.")




# without self  give an error
# TypeError: Without_Self.without_self() takes 0 positional arguments but 1 was given

class Without_Self:
    # def without_self():
    #     print("Without Self :")
    def without_self(self):
        print("With Self :")
        
        
        
without_self_obj=Without_Self()
without_self_obj.without_self()
        


#how to prove that self is pinting to the current object


class Prove_Self:
    def prove_self(self):
        print("Address Of The Self:",id(self))
        
        

prove_obj=Prove_Self()
prove_obj.prove_self()
print("Address of the object:",id(prove_obj))

#both are pinting to the same memory location that's prove that they are pointing to the current object.




#self are not accessile outside of the class 


class Self_Outside:
    def self_outside(self):
        print("Self Access Inside The Class:",self)
        print("Object Acessing Inside the class:",self_in_class)
    

self_in_class=Self_Outside()
self_in_class.self_outside()
#accessing the self outside of the class
#NameError: name 'self' is not defined.
# print("Self Outside of the Class:",self)

