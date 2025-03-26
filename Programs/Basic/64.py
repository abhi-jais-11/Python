#Write a program to find the common elements between two tuples.

def common_element_tuple(tpl_1,tpl_2):
    return tpl_1 and tpl_2


#driver code 
tpl_1=(1,2,3,4,5)
tpl_2=(4,5)

common_element=common_element_tuple(tpl_1,tpl_2)

print(f"Common Element In tuple are: {common_element}")