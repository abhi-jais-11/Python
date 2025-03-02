
#defining a function that check number is armstrong or not


def Is_Armstrong(num):
    p=len(str(num))
    rem=0
    sum=0
    while num >0:
        rem=num%10
        sum=sum+rem**p
        num=num//10
    return sum
        

num=int(input("Enter The Number To Check Armstrong Or Not:"))

if num==Is_Armstrong(153):
    print(f"{num} Is Armstrong:")
else:
    print(f"{num} Is Not Armstrong:")
