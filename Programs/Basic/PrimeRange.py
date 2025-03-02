
#defining function to check nums is prime or not 

def Is_Prime(num):
    sqr=(num**.5)
    is_prime=True
    
    for i in range(2,int(sqr+1)):
        if num%i==0:
            is_prime=False
    return is_prime



rng=int(input("Enter the Range to Check Prime:"))
for num in range(1,rng+1):
    if Is_Prime(num):
        print(f"{num} Is Prime:")
    else:
        # print(f"{num} Is Not  Prime:")
        pass
