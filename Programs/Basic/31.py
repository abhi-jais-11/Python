#measure the execution time 

from time import time

st=time() #start time

for i in range(1,101):
    if i%5==0:
        pass
    

et=time() #end time 
print()
print()
print(f"Time Taken By Program:{et-st}")