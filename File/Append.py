#append mode does not  overrite the old content.
# with open("append.txt",'a+') as file:
#     file.writelines(["Hello\n","Hii, I'm Abhinav Jaiswal.\n","I'm From Basti UP.\n","I Have Done B.Tech from BIET Lucknow.\n"])



#readind file which is append .

with open("append.txt",'r') as file :
    print(file.read()) # it read whole file at once .

# print(file.read())ValueError: I/O operation on closed file./