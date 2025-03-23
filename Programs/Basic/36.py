from random import randint
from time import time

lst=[]

for i in range(1,1001):
    lst.append(randint(1,1000))

st=time()
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i] 
et=time()
print(f"Time Taken By The Program To Sort The 1000 Random Element In List:{et-st}")

