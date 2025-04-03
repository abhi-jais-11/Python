#recursive function to count the number of digit .

def count_digit(n,count=0):
    if n<=0:
        return 0
    return count+1 + count_digit(n//10,count)
        


#function call
n=1234567891
ans=count_digit(n)
print(f"No of digit in {n} is : {ans}")