'''
1.fromkeys()
    -Creates a dictionary from the given sequence

'''
dct={
    "name":"jack",
    "age":21,
    "mail":"xyz@gmail.com"
}
new=dct.fromkeys(['name','age','mail'])
print(new)




'''
Python Dictionary items() method
As of Python 3.7, dictionaries are ordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, a Dictionary holds a key: value pair.
In Python Dictionary, items() are the list with all dictionary keys with values.
 
Syntax: dictionary.items()
Parameters: This method takes no parameters.
Returns: A view object that displays a list of a given dictionary’s (key, value) tuple pair.

'''

print('-------------------------')
key_value=dct.items()
print(key_value)

print('-----------------------------')



'''
keys()
Returns a view object that displays a list of all the keys in the dictionary in order of insertion

values()
Returns a view object containing all dictionary values, which can be accessed and iterated through efficiently
'''

print(dct.keys())
print(dct.values())
print('-----------------------')



'''
update()
Updates the dictionary with the elements from another dictionary or an iterable of key-value pairs.
With this method, you can include new data or merge it with existing dictionary entries

'''
dct.update({"phone":"+91 8957889130","id":20,"Address":"Marlin In Switzerland"})
print(dct)
print(dct)
print('------------------------------')
