#lambda function to check even number
even = lambda x: x%2==0


num=10
if even(num):
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
