'''
Static Methods:

key Point
    No self or cls parameter: Static methods do not take self (instance) or cls (class) as the first argument.
    Bound to the class, not the instance: They are called on the class itself, not on an instance of the class.
    Utility functions: Often used for functionality that is related to the class but does not need access to instance or class-specific data.
    Static methods are defined using the @staticmethod decorator and are typically used for utility functions that do not depend on the state of the class or instance.
When to Use Static Methods:
    -When the method does not need to access or modify the class or instance state.
    -When the method is a utility function that logically belongs to the class but does not depend on class-specific data.
    -When you want to group related functions under a class namespace.

'''

#static method for math 


class Calculator:
    
    @staticmethod
    def add(*args):
        nums=list(args)
        print(f"Sum Of the Nums: {sum(nums)}")
    
    @staticmethod
    def mul(*args):
        res=1
        for i in args:
            res*=i
        print(f"Multiplication of Nums is :{res}")
    
    @staticmethod
    def div(a,b):
        if b!=0:
            print(f"Division Of the Num is :{a/b}")
            
    @staticmethod
    def power(n,p):
        print(f"Power Of the Nums is :{n**p}")
        
    

            


calc=Calculator()
calc.add(1,2,3,4,5,6,7,8,9,10)
calc.mul(1,2,3,4,5)
calc.div(10,2)
calc.power(10,2)


