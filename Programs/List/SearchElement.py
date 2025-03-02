
#seacrh elemet in the list

def search_element(lst,num):
    if num in lst:
        return lst.index(num)
    else:
        return -1
    

lst=[1,2,3,10,26,10,22,39,4,5,6]
num=22
ans=search_element(lst,num)

if  ans!=-1:
    print(f"Element Present At Index :{ans}")
else:
    print(f"Element Not  Present in List:")