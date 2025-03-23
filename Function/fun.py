
'''

Function:

    - Block of code to perform a specific task.

    Syntax: 
            #formal parameter
        def function_name(parametre/argument):
                """
                Doctring 
                """
                #block code 
                
                return statement 
                    #not execute 

        #function call
        #function_name(parametr,) 
            #actual parameter              

'''

# with return 
# without return 


#simple function 



def greet():
    '''
    Simple function to greet 
    '''
    print(f"Hello Welcome")
    


#how to access
# print(greet.__doc__) #magic varible __var_name__ 

# #function call

# greet()


#
def greet(name):
    '''
    This is greet function to somone...
    '''
    print(f"Hello Welcome : {name}")


#
# greet("Jack")
# greet() #TypeError: greet() missing 1 required positional argument: 'name'



# 
def greet(name):
    return f"Hello Welcome {name}"


#
# name=greet("Jack") # f"Hello Welcome {name}"
# print(name)
# print(greet("Jacksone"))




'''

Type of args:

    1.Default 
    3.Positional
    3.keywords
    4.atbitry/varibale length [*args,**kwargs]


'''



#1.Default

def student_info(id=1,name="Jack",age=18):
    
    print(f'Id:{id}\nName:{name}\nAge:{age}')
    


#function call
# student_info(10,"Jack",22)
# student_info(10,)
# student_info(10,"Jacksone")
# student_info(10)
# student_info(0,None,22)


#2.Positional

def student_info(name,age):
    print(f"Name:{name}\nAge:{age}")
    


# student_info("Jack",22)
# student_info(22,"Jack") #
# student_info("jack") # TypeError: student_info() missing 1 required positional argument: 'age'


#3.keyword argumet

def student_info(name,age):
    
    
    print(f"Name:{name}\nAge:{age}")
    
    
    
    
# student_info(name="Jack",age=22)
# student_info(age=22,name="Jack")



'''
4.varibale length 
    1.*args
    2.**kwargs

'''
# def add(a,b):
#     print(a,b)

# add(10,20)
# add(10,20,20)




def nums(*args): #args type ==>tuple
    
    print(f"{len(args)}")



#
# nums()
# nums(1,2,3)
# nums(1,2,3,45,6)


def student_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        

#
# student_info(name="Jack",age=23,email="jack12@gamil.com")


def info(name,age):
    return name,age

# name=input("Enter Name:")
# age=int(input("Enter Age:"))

# name,age=info(name=name,age=age)

# print(f"Name:{name} and Age:{age}")



# 
def factorial_of_number(n):
    res=1
    if n==0:
        return 1
    #iteration
    for i in range(1,n+1): #1,2,3,4,5 [5+1-1=5]
        res=res*i

    return res
    
    
# num=int(input("Enter The number:"))
# ans=factorial_of_number(num)

# print(f"Factorial of {num} is :{ans}")

'''
Type of funtion:    
        -Built - in  Function.
        - User define
        -ananymous
        -recursive

'''
#1.Buil-in function

# print(type(10)) #type 
# x=10
# print(id(10)) #address 

# for i in range(97,123):
#     print(chr(i),end=" ")
# print()
# print(ord('A')) #65



# a funtion  without name 


    
    