'''
Methods of dictionary:
        1.fromkeys()
        2.update()
        3.keys()
        4.values()
        5.item()
        6.pop()
        7.popitem()
        8.clear()
'''
'''
1.fromkeys(iterable,value to each element same) #Create a new dictionary with keys from iterable and values set to value:
Value of each key deault is None 

'''
dct={}
dct=dct.fromkeys(["id","name","age","city"])
print(dct)

print('---------------------------------------')

'''
2.update()  #add the multiple element in the dictionary


'''
dct.update(id=3,name="Jenna",age=22,city="America")
#or
dct.update({'id': 3, 'name': 'Jenna', 'age': 22, 'city': 'America'})
print(dct)

print('---------------------------------------')


'''

3.Keys() Return a set-like object providing a view on the dict's keys.


'''
print(dct.keys())


print('-------------------------------------------')
'''

4.values() Return a set-like object providing a view on the dict's values.


'''
print(dct.values())

print('-------------------------------------------')
'''

5.items()Return a set-like object providing a view on the dict's items.


'''
print(dct.items())

print(dct.values())

print('-------------------------------------------')
'''

6.pop(key)  #remove and return value using the key

'''
print(dct.pop("city"))


'''

7.popitem()  #remove last key,value pair and return tupe of key ,value 

'''
print(dct.popitem())





'''

7.clear()  # clear dictionary 

'''
print(dct.clear())

