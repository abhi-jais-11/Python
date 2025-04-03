#rcursive function to find the sum of the digit of a number

def sum_of_digit(num):
    if num==0:
        return 0
    else:
        return  (num%10) + sum_of_digit(num//10)


#function call
num=151
ans=sum_of_digit(num)
print(f"Sum of digits of {num} is : {ans} ")
