'''
Keywords in Python ?
    -Python keywords are reserved words that have special meanings and serve specific purposes in the language syntax. -Python keywords cannot be used as the names of variables, functions, and classes or any other identifier.

Getting List of all Python keywords
'''
import keyword
print(keyword.kwlist)


'''
1.Value Keywords	
        -True, False, None
'''
print(True==1)
print(False==0)
print("---------------------")
print(True+1)
print(True+0)
print("---------------------")
print(False+1)
print(False+0)
print("---------------------")
print(None==0)
print(None==False)
print(None==None)
print('--------------------')

'''
2.Operator Keywords	
    - and, or, not, in, is
'''
print(True and True) # true 
print(True and False) # false 
print(False and False) # false
print('----------------------')
print(True or False) # true
print(True or True) # true
print(False or False) # false
print('----------------------')
print(not True) # false
print(not False) # true
print('----------------------')
print(2 in [1,2,3,4,5])  #True in only check value 
print(4.5 in [1,2,3,4,5]) # false
print('s' in 'strlangeugfyhs') #True
print('----------------------')

print([1,2,3] is [1,2,3]) # false is check the reference of the varibale 
print([1,2,3] == [1,2,3]) # false it ckeck the value of the valiable