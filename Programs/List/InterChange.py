
#interchange first element to last element

def Inter_Change(lst):
    lst[0],lst[len(lst)-1]=lst[len(lst)-1],lst[0]
    return lst


#lst
lst=[1,2,3,4,5,6,7,8]

print(f"Before Inter Change List :{lst}")
print(f"After Inter Change List:{Inter_Change(lst)}")