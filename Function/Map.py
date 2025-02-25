'''
Python map() function
    The map() function is used to apply a given function to every item of an iterable, such as a list or tuple, and returns a map object (which is an iterator).
    syntax:
        map(function, iterable)
'''

# square of the number 

def square(n):
    return n**2


nums=list(map(square,[1,2,3,4,5]))

print(nums)


# using lambda funtion


arr=[1,2,3,4,5,6]

num=list(map(lambda x: x**2 ,arr ))
print(num)



name=['jack','amit','raj']
name_upper=list(map(str.upper,name))
name_cpital=list(map(str.capitalize,name))
print(name_upper,name_cpital)