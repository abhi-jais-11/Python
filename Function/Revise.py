def login_function(func):
    def wrapper(name):
        if name!=True:
            print("Login Required")
        else:
            func(name)
    return wrapper


@login_function
def main(name):
    print("User is login")

# main(True)
# main(False)







# square_nums=(num for num in range(1,100000000000000000001))
