#Write a program to remove all duplicate elements from a list without using sets.

def remove_duplicate(lst):
    original_lst=[]
    for i in lst:
        if i not in original_lst:
            original_lst.append(i)
    return original_lst


#driver code 
lst=[1,2,2,3,4,5,5]
print(f"Before Removing Duplicate: {lst}")
ans=remove_duplicate(lst)
print(f"After Removing Duplicate: {ans}")