
def copy_list(lst):
    new_list=lst #deep
    new_lst=lst.copy()#shallow 
    return new_list,new_lst


print(*copy_list([1,2,3]))