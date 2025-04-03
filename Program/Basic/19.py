#recursive function to find the sum of the list  element
def sum_elements(lst,sum=0):
    if len(lst) == 0:
        return 0
    return sum+lst[0] + sum_elements(lst[1:],sum)


#fucntion call
lst=[19,20,20,21]
ans=sum_elements(lst)
print(f"Sum of list {lst} is :{ans}")