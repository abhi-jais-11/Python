#Write a program to sort a dictionary by its values in descending order.
def sort_dct(dct):
    sorted_dict = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


dct = {'apple': 50, 'banana': 30, 'cherry': 40, 'date': 10}
sorted_dict = sort_dct(dct)
print("Sorted Dictionary:", sorted_dict)
