#Write a program to find the intersection of two lists without using sets.

def intersect_list(lst_1,lst_2):
    return lst_1 and lst_2

#driver code 

lst_1=[1,2,3,4,5]
lst_2=[4,5]

intersect_lst=intersect_list(lst_1,lst_2)

print(f"Intersection of the list is : {intersect_lst} ")