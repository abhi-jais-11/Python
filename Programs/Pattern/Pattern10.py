row=int(input("Enter The Size:"))
for _ in range(1,row+1):
    if _<=row:
        print(" "*(_)+" *", sep="") 
    if _<=row:
        print(" "*(row-_)+" * ")
 