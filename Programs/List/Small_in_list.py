
# minimum in list 

def min_in_list(lst):
    
    #1.using min ()
    # return min(lst)
    
    #2.sort()
    # lst.sort()
    # return lst[0]
    
    #3.using for loop 
    small=lst[0]
    for i in lst:
        if small > i:
            small=i
            
    return small
    


#list 
lst=[8,2,100,29,20,17,10,1]
print(min_in_list(lst))

