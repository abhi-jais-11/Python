'''
Inner funtion
    A function that is defined inside another function is known as the inner function or nested function. 
    Nested functions can access variables of the enclosing scope. 
    Inner functions are used so that they can be protected from everything happening outside the function.
'''

def outer(name):
    greet=f"Welcome {name}"
    def inner():
        return greet
    return inner()

print(outer("Abhinav"))


def outer_func(n,m):
    def inner_fun(m):
        return n+m
    return inner_fun(m)

print(outer_func(10,20))



