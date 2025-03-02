row=int(input("Enter the Number of rows:"))
col=int(input("Enter the Number of columns:"))

for i in range(row):
    for j in range(row):
        if i==0 or i==row-1 or j==0 or j==col-1 :
            print("*" ,end =" ")
        else:
            print(" ", end=" ")
    print()