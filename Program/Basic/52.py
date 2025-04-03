#find the 2nd max value in the list 

def find_max(lst):
    
    lst=sorted(lst)
    return lst[len(lst)-2]

#driver code 
lst=[1,28,30,78,98,12]

print(f"Max value in the list is : {find_max(lst)} ")