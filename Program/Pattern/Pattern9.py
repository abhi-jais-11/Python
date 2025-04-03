row=int(input("Enter The Size:"))
for _ in range(1,row+1):
    if _==row//2:
        print(" *"*(row),sep="") 
    else:
        print("  "*(row//2)+"*")
