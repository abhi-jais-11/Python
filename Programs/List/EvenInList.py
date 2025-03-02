
#even in list 

def even_in_list(lst):
    
    return list(filter(lambda i :i%2==0,lst))


#list 
lst=[i for i in range(1,11)]
print(f"Even in List:{even_in_list(lst)}")