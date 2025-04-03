#function to find the average of the list element

def avg_of_elements(lst):
    return sum(lst)/len(lst)



#function call
lst=[10,2,19,20,45]
ans=avg_of_elements(lst)
print(f"Avrage of the list {lst} is : {ans}")