
def cube_of_n_numbers(n):
    return n**3



n=int(input("Enter the  Range :"))
for i in range(1,n+1):
    print(cube_of_n_numbers(i),end=" ")