#Write a program to reverse a tuple without using slicing

def reverse_tuple(tpl):
    rev_tpl=reversed(tpl)
    return tuple(rev_tpl)



#driver code
tpl=(10,20,30,40)
rev_tpl=reverse_tuple(tpl) 
print(f"Reverse of the Tuple is : {rev_tpl}")