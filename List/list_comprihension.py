'''
List Comprehension in Python

    -List comprehension is a way to create lists using a concise syntax. 
    -It allows us to generate a new list by applying an expression to each item in an existing iterable (such as a list or range). 
    -This helps us to write cleaner, more readable code compared to traditional looping techniques.
    
    Syntax:
      [expression for item in iterable if  condition (optional)]
      
      expression variable name , item name and use variable  in condition  must be the same name 
      else it generate error.
      
      expression: The transformation or value to be included in the new list.
      item: The current element taken from the iterable.
      iterable: A sequence or collection (e.g., list, tuple, set).
      if condition (optional): A filtering condition that decides whether the current item should be included.
'''

#using the list comprihension creating a list of square's 1-10:

square_nums=[i**2 for i in range(1,11)]
print(square_nums)

print('-----------------------------------')
#filtering the even from the list 
even_list=[even  for even in square_nums if even%2==0]
print(even_list)

print('-----------------------------------')
lst_30_nums=[*range(1,31)]
print(lst_30_nums)

print('-----------------------------------')
#filtering odd from the list 
odd_list=[odd for odd in lst_30_nums if odd%2 !=0]
print(odd_list)


print('-----------------------------------')
#filtering even from the list 
even_list=[even for even in lst_30_nums if even%2 ==0]
print(even_list)


#filtering the perfect square 1-31

perfect_square_root=[int(psq**.5) for psq in range(1,31) if psq**.5 == float(f"{psq**.5 :.1}".format(psq**.5)) ]
print('-----------------------------------')
print(perfect_square_root)



print('-------------------------------------')

#filtering the list of nums form 1-50 if divisible by 5

divide_by_five=[nums for nums in range(1,51) if nums%5==0]
print(divide_by_five)


