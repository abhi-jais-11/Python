row=int(input("Enter the Number of rows:"))
col=int(input("Enter the Number of columns:"))

for i in range(row):
    for j in range(col-i):
        print(" ",end=" ")
        
    for k in range(i+1):
        print("*",end=" ")
    print()
    