'''
Dictionaries in Python
    -A Python dictionary is a data structure that stores the value in key: value pairs.
    -Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.
    
Way to create :
    1.Using {}
    2.Using DictionaryConstructor
    
'''
#1. using {"key":"value"}
dct_bracket={}
print(dct_bracket)
print('----------------------')

#using dict(key=value)

dct_const=dict()
print(dct_const)
print('----------------------')


#adding the element
dct_bracket={
    "Id":3,
    "name":"Jenna",
    "Age":22,
    }

print(dct_bracket)

print('------------------------------')


dct_const=dict(id=3,name="Jenna",age=22)
print(dct_const)


print('------------------------------')

#using assignment 

dct={}

dct["id"]=3
dct["name"]="Jenna"
dct["age"]=22

print(dct)



print('---------------------------')

'''
Way to access the element of the dictionary:
        1.Using dct[Key]
        2.Using get("key")
        3.using loop
        
'''
#using key
print(f"Id:{dct["id"]}\nName:{dct["name"]}\nAge:{dct["age"]}")

print('----------------------------------------------------')

#using get("key")
print(f"Id:{dct.get("id")}\nName:{dct.get("name")}\nAge:{dct.get("age")}")

print('----------------------------------------------------')

#using get("key")
for key in dct:
    print(f"{key.capitalize()}:{dct[key]}")

