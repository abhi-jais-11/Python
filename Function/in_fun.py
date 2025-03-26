
def outer():
    name="Outer"
    # Nested functions can access variables of the enclosing scope.
    def inner():
        print(name)
    
    return inner


outer()()


