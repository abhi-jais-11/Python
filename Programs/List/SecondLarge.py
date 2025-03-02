
# second large in list 

def max_in_list(lst):
    lst.sort()
    return lst[len(lst)-2]


lst=[8,2,100,29,20,17,10,1,200]
print(max_in_list(lst))

