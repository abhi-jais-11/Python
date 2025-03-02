row=int(input("Enter the Number of rows:"))
col=int(input("Enter the Number of columns:"))

for i in range(row):
    for j in range(col-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        if i==0 or i==row-1  or k==0 or k==2*i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    