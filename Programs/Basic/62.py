def sum_even_numbers(nested_list):
    total = 0
    def find_even_numbers(sublist):
        nonlocal total
        for item in sublist:
            if isinstance(item, list):  
                find_even_numbers(item)  
            elif isinstance(item, int) and item % 2 == 0: 
                total += item

    find_even_numbers(nested_list)
    return total

#driver code 
nested_list = [1, 2, [3, 4, [5, 6], 7], 8, [9, 10]]
result = sum_even_numbers(nested_list)
print("Sum of all even numbers:", result)