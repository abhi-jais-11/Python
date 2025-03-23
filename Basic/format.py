'''
format()
    : format() method the pefified values and insert them inside the string's placeholder .
    : The placeholder is define using curly brackets {}.
    : The format() method return the formated string.

syntax: 
        string.format(var1,var2,........)
'''
name="Jackson"
age=22

print("Name : {name} and Age : {age} ".format(name="Jack",age=21))
print("My name is {} , I'm {} year old".format(name,age))
print("My name is {0} , I'm {1} year old".format(name,age))


#formate specifiers ....

num=1000
print("The Price of the Product is{:.3f} :".format(num)) #float 
print()
print("The Price of the Product is {:d} :".format(num)) #integer
print()
print("The Price of the Product is {:,} :".format(num)) # seprate with comma
print()
print("The Price of the Product is {:_} :".format(num)) # seprate with _
print()
print("The Price of the Product is {:b} :".format(num)) # binary representation
print()
print("The Price of the Product is {:c} :".format(num)) #unicode char.
print()
print("The Price of the Product is {:e} :".format(num))
print()
print("The Price of the Product is {:E} :".format(num))
print()
print("The Price of the Product is {:f} :".format(num)) #float
print()
print("The Price of the Product is {:g} :".format(num))  #general format
print()
print("The Price of the Product is {:G} :".format(num)) #general
print()
print("The Price of the Product is {:o} :".format(num)) #octal
print()
print("The Price of the Product is {:x} :".format(num)) #hexa 
print()
print("The Price of the Product is {:n} :".format(num)) #number format
print()
print("The Price of the Product is {:%} :".format(num)) # % format
print()