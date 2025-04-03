#function to check num is even or odd

def is_even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"


#function call
num=10
ans=is_even_odd(num)
print(f"{num} is {ans}")