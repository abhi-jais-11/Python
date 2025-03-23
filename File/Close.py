file=open("append.txt",'r') 
cnt=file.read()
print(cnt)
file.close()
cnt=file.read()
# print(cnt) ValueError: I/O operation on closed file.