
# maximum in list 

def max_in_list(lst):
    
   # 1.using max ()
    # return max(lst)
    
    #2.sort()
    lst.sort()
    return  lst[len(lst)-1]
    
    # #3.using for loop 
    # max=lst[0]
    # for i in lst:
    #     if max < i:
    #         max=i
    # return  max
    


#list 
lst=[8,2,100,29,20,17,10,1]
print(max_in_list(lst))

