'''
File Handeling:
    -File handling refers to the process of performing operations on fle such as creation , opening ,reading , writing and closing through the programing interface.

Function of the file :
    - open("file" ,"mode") : use for the open the file with a specific mode .
    
    => File you want to open with path ex demo/file/demo.txt
    => mode is defines the opration on the file such as :
        -read 
        -write
        -append 
        -write and  read  and so on.....
        
Mode of the file :

    r  : read only mode 
    rb : read in banary modde  
    r+ : read and write mode 
    rb+: read and write in binary mode
    
    w  : write only mode 
    w+ : write and read  mode 
    wb+: write and read in binary mode.
    
    a  : append mode 
    ab : append in banary mode.
    a+ : append and read mode .
    
    x :exclusive creation mode if already exist give an error.
    xb:exclusive creation of  binary 
    x+:exclusive creation and read and write mode  
    xb+:exclusive creation in binary  and read and write mode  .
    
    
    



'''

#opening file 
'''
1. we can open a file two ways .
'''
#1. without with statement  
# we need to close the file at the end of the operation if we r not using the with statement.

file = open("demo.txt","r+")
file.write("Hello This is Demo Text.") # overwrite the previous content. write()
file.seek(0)  # it is use to set the pointer while move from the start .
text=file.read()
print(text)
file.close()



#with - with statement -> We dont need to close the file while using the with statement it is manage by the with.

with open("demo.txt","r+") as file: #you can take any name at the place of the file
    text=file.read()
    print(text)
