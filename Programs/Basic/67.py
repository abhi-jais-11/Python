def find_smallest_missing_positive(nums):
    
    nums = [num for num in nums if num > 0]  
    
    nums = sorted(set(nums))  
    smallest_missing = 1
    
    for num in nums:
        if num == smallest_missing:
            smallest_missing += 1
        else:
            break
    return smallest_missing



#driver code 
nums = [3, 4,1,1,2, 6]
result = find_smallest_missing_positive(nums)
print("The smallest missing positive integer is:", result)