#function to find the max value in list using recursive function

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        m = find_max(lst[1:])
        return m if m > lst[0] else lst[0]


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans=find_max(lst)
print("The maximum value in the list is:",ans)