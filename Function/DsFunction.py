
def add(a,b):
    print("Sum:",a+b)

def sub(a,b):
    print("Sub:",a-b)
    
    
func={
    "add":add,
    "sub":sub
}

func.get("add")(10,20)
func.get("sub")(20,10)
