
#multipy of element in list

def multipy_element(lst):
    res=1
    for i in lst:
        res*=i
    return res
    






lst=[1,2,3,4,5]
print(f"Multiplication of the Numbers of the list is :{multipy_element(lst)}")