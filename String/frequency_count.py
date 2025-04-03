from str_module import count_frequency

str=input("Enter String To Count The Frequency of Char:")

dct=count_frequency(str)

print("Frequency Of Each Char is :")
for key,value in dct.items():
    if key !=" ":
        print(f"{key} = {value}")


#or 
# print("Frequency oc Each Char is : {}".format(count_frequency(str)))
