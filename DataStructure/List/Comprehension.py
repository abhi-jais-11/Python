'''
List Comprehension in Python

    -List comprehension is a way to create lists using a concise syntax. 
    -It allows us to generate a new list by applying an expression to each item in an existing iterable (such as a list or range). 
    -This helps us to write cleaner, more readable code compared to traditional looping techniques.
    
    Syntax:
      [expression for item in iterable if condition]
        expression: The transformation or value to be included in the new list.
        item: The current element taken from the iterable.
        iterable: A sequence or collection (e.g., list, tuple, set).
        if condition (optional): A filtering condition that decides whether the current item should be included.
'''
lst=[ i for i in range(1,31)]
print(lst)
print('----------------------------')

#even from the list
even_list=[even for even in lst if even %2==0]
print("Even Number list:\n",even_list)\
    
    
    
print('----------------------------')

# odd from the list
odd_list=[odd for odd in lst if odd %2!=0]
print("Even Number list:\n",odd_list)



#square of each element in the list
print('----------------------------')
square_list=[val**2 for val in lst]
print("Square of each elememnt in list:\n",square_list)


# max value from the list
max_value=[max(*lst)]
print(max_value)

print('-------------------------------')
#min value from the lst
min_value=[min(*lst)]
print(min_value)


#sum value of the list

print('-------------------------------')
sum_value=[sum(lst)]
print(sum_value)