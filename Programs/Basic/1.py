# function to calculate the factorial of number

def factorial_num(n):
    res=1
    if n<=1:
        return 1
    else:
        for i in range(1,n+1):
            res*=i
        return res



#function call
num=5
ans=factorial_num(num)
print(f"Factorial of {num} is :{ans}")

        
        
    