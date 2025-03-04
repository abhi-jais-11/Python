
#opening file 

'''
Reading a File
    Reading a file can be achieved by file.read() which reads the entire content of the file.
    After reading the file we can close the file using file.close() which closes the file after reading it, which is necessary to free up system resources.
'''
file =open("file.txt","r")
content=file.read()
print(content)
file.close()


#reading file in binary mode

file =open("file.txt","rb")
content=file.read()
print(content)
file.close()

print("-------------------------------------- ")
#using with statement  we don't need to close it ,auto handle by with .


with open("file.txt","r") as file:
    content=file.read()
    print(content)