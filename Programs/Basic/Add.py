
#defining a function who rertun the sum of the numbers

def add(list):
    return sum(list)


length = int(input("How Many Number You Want Add :"))
list=[]
for i in range(1,length+1):
    num=int(input("Enter The Numbers %d:"%i))
    list.append(num)

print(f"Sum is:{add(list)}")
    