#recursive function to find the power of a number
def power_nums(num,pow):
    if pow==0:
        return 1
    return num*power_nums(num,pow-1)

#functionn call
num=5
ans=power_nums(num,2)
print(f"Power of {num} is : {ans}")