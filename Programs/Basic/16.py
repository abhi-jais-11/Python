#recursive function to find the  gcd

def gcd_nums(n1,n2):
    if n2 ==0:
        return n1
    
    return gcd_nums(n2,n1%n2)



#function call
num1=4; num2 =34
ans=gcd_nums(num1,num2)
print(f"Gcd of {num1} and {num2} is : {ans}")
