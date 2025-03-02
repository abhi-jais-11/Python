
#sum of the elementof the list

#1 using sum()
#2.using loop


def sum_of_element(lst):
    # return sum(lst) comment loop if use it
    
    #using loop 
    sum=0
    for i in lst:
        sum+=i
    return sum




lst=[1,2,3,4,5,6,7,8,9,10]#55

print("Sum fo The List is : ",sum_of_element(lst))
