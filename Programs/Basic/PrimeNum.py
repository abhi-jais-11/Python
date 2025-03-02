
#defining function to check nums is prime or not 

def Is_Prime(num):
    sqr=(num**.5)
    is_prime=True
    
    for i in range(2,int(sqr+1)):
        if num%i==0:
            is_prime=False
    return is_prime



num=int(input("Enter the Number to Check Prime:"))

if Is_Prime(num):
    print(f"{num} Is Prime:")
else:
    print(f"{num} Is Not  Prime:")
