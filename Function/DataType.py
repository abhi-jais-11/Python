
'''
Explicitly Define parameter

'''

# it can take any type of value 
def sum(a:int , b:int)->int:
    return a+b

print(sum(10,29))
print(sum('10','20')) # it is string 
print(sum(20.5,10.29))


# for preventing this need 

print('---------------------------------------')
def Sum(a:int , b:int)->int:
    """ Both arguments must be integer """
    assert isinstance (a,int) and (b,int)
    return a+b

print(Sum(10,20))
# print(Sum("20","29")) generate an error
