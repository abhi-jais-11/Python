
#factorial of number

def Factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

num=int(input("Enter The Positive Integer To Calculate Factorial:"))

print(f"Factorial Of Number Is:{Factorial(num)}")