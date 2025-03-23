#measure the execution time 

from time import time

st=time() #start time

for i in range(1,1001):
    pass
    
et=time() #end time 
print(f"Time Taken By Loop 1000 Time:{et-st}")