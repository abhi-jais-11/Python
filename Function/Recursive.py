'''
Recursive Functions in Python
    -Recursion in Python refers to when a function calls itself. 
    -There are many instances when you have to build a recursive function to solve Mathematical and Recursive Problems.
Using a recursive function should be done with caution, as a recursive function can become like a non-terminating loop. 
It is better to check your exit statement while creating a recursive function.

'''

#factorial fo the number 

def fact_num(n):
    if n==0: #base case
        return 1
    return n*fact_num(n-1)


n=int(input("Enter the Number:"))
print(f"Factorial of the number is:{fact_num(n)}")


# sum of n number 

def sum_num(n):
    if n<0: #base case
        return 0
    return n+sum_num(n-1)

print(f"Sum of {n} is {sum_num(n)}")
    