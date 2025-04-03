#recursive  function to calculate the factorial of numaber

def factorial_num(n):
    if n<=1:
        return 1
    return n*factorial_num(n-1)


#function call
num=5
ans=factorial_num(num)
print(f"Factorial of {num} is : {ans}")