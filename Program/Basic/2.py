#function to chek number is prime or not

def is_prime(num):
    is_prime=True
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            is_prime=False
    return is_prime


#function call
num=10
ans=is_prime(num)
if ans:
    print(f"{num} is Prime :")
else:
    print(f"{num} is not Prime :")
    
            