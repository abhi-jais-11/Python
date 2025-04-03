# function to find maximum of three numbers

def max_value(*args):
    return max(args)


# function call
num1=10;num2=-10;num3=200
ans=max_value(num1,num2,num3)
print(f"Max value of {num1},{num2},{num3} is : {ans}")
