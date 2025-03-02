
#defining function that return fibbonacci of nth term

def fibbonacci(num):
    if num<=1:
        return num
    else:
        return fibbonacci(num-1)+fibbonacci(num-2)
    

ntht=int(input("Enter the Positive Number:"))

print(f"Fibbonacci fo the number is:{fibbonacci(ntht)}")