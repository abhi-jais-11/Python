'''
Dictionaries in Python
    -A Python dictionary is a data structure that stores the value in key: value pairs.
    -Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.
    
'''

'''
1.How to Create a Dictionary
In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by a ‘comma’.

'''
# create dictionary using { }
dct={'a':'jack','b':'John'}
print(dct)

# create dictionary using dict() constructor
dct=dict(a="Jack",b="John")
print(dct)

print('-------------------------------------------------------------')


'''
2.Accessing Dictionary Items
We can access a value from a dictionary by using the key within square brackets or get()method.
'''

dct={
    "name":"Jack",
    "age":23,
    "email":"jack112@gmail.com",
    "id":20
}

#using [] backect
print("Id:",dct["id"])
print("Name:",dct["name"])
print("Age:",dct["age"])
print("Email:",dct["email"])

print('-----------------------')
#using get()
print(f"Id:{dct.get("id")}")
print(f"Name:{dct.get("name")}")
print(f"Age:{dct.get("age")}")
print(f"Email:{dct.get("email")}")

print('------------------------------------------------------------------------')

for _ in dct:
    print(f"{_}={dct.get(_)}")

print('---------------------')
'''
3.Adding and Updating Dictionary Items
We can add new key-value pairs or update existing keys by using assignment.

'''

dct["phone"]="+91 8957889130"
print(dct)


print('------------------------')
'''
4.Removing Dictionary Items
    We can remove items from dictionary using the following methods:
    del: Removes an item by key.
    pop(): Removes an item by key and returns its value.
    clear(): Empties the dictionary.
    popitem(): Removes and returns the last key-value pair.

'''
#pop()
print(dct.pop("email"))
print(dct)

#del

del dct["id"]
print(dct)

#popitem()
print(dct.popitem())


#clear()
dct.clear()
print(dct)
print('---------------------------------')