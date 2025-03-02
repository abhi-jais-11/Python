#negative in list

def negative_in_list(lst):
    
    return list(filter(lambda i :i<0,lst))

#list 
lst=[1,2,3,-3,-5,-1,-18,20]
print(f"Negative in List:{negative_in_list(lst)}")


