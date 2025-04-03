# a=''
# print(bool(a))


#IndexError:
        #when we accessing the index value out of range of list.
        #ex list=[1,2,34]==>list[3]#indexerror
        
lst=[1,2,3]
# print(lst[3])#IndexError: list index out of range
print(lst[2]) #3

print('------------------------------------')



#KeyError :
        #when we access the value of the dictionary using key 
        #who is not present in the dictionary it ocuures.
        #ex dct={"name":"jack"}==>dct.["age"]#keyerror
        

dct={"name":"jack"}
# age=dct["age"]#KeyError: 'age'
# print(age)


print('-------------------------------------------')

#TypeError :
        #whe we perform the opertion on arithmetic operation.
        #and unsupported operand type
        #ex. 10+"Hello"==>typeerro


#for check uncomment the code 

# print(10+"Hello")#TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print("hello"+True) #TypeError: can only concatenate str (not "bool") to str


print('---------------------------------------------------------')

#ValueError:
        #whe we want to convert the one data type to another that is not valid coversion it occurs.
        
        #ex "jack"==>int("jack") 
        #string can be convert in bool
        

# print(int("jack"))ValueError: invalid literal for int() with base 10: 'jack'

print(bool("name")) #True
print(list("name")) # ['n', 'a', 'm', 'e']

# print(dict("name"))ValueError: dictionary update sequence element #0 has length 1; 2 is required

        


#FileNotFound:
        #when we accees the file that is not extst it will ocuures.
        #ex:open('file.txt','r)==>FileNotFound.
        
        
# with open('file.txt','r') as file:
#     print(file.read())
    
# FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'



#