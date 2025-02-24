'''
1.Write a program to generate the n number
'''
n=int(input("Enter the number of term:"))
for i in range(1,n+1):
    print(i,end=" ")

print()
'''
2.white a program to calculate the sum of n number:
'''
num=int(input("Enter the number :"))
sum=0
for i in range(1,num+1):
    sum+=i
print(sum)

for i in [1,2,3,4,5,6]:
    print(i, end=" ")
print()


for key , value in {"name":'jack',"age":21,"id":3}.items():
    print(f"{key} = {value}")
    