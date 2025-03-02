

#count occurence of element

def count_occurence(lst,num):
    
    # 1.return lst.count(num)
    #2.using loop
    count=0
    for i in lst:
        if i==num:
            count+=1
    return count


#lst
lst=[1,2,3,3,3,3,3,3,4,5]
num=3
print(f"Occurence of {num} in lsit is : {count_occurence(lst,num)}")
    

