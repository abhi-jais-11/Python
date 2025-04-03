#function to calculate the fibbonacci sequence up to nth term using recursion

def fibb_series(n):
    if n<=1:
        return 1
    else:
        return fibb_series(n-1)+fibb_series(n-2)


#function call
num=6
ans=fibb_series(num)
print(f"Fibbonaci up to {num}th term is : {ans}")

