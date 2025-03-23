'''
We can write a file with using the write() and witelines() funtion

==>write() funtion take a string exactly one argument .
==> weritelines() function take a sequence of string :[iterable such as :==> list , tuple , set etc..]

==>write() function override the previous content.
==>writelines() function override the previous content.

'''

#write () 
with open("demo.txt","w+") as file:
    file.write("When dealing with non-text data (e.g., images, audio, or other binary data), Python allows you to write to a file in binary mode. Binary data is not encoded as text, and using binary write mode  ensures that the file content is handled as raw bytes.")
    file.seek(0)
    data=file.read()
    
    print(data)
    
print("==================================================")

#witelines()

#list
with open("demo.txt","w+") as file:
    file.writelines(["When dealing with non-text data (e.g., images, audio, or other binary data).\n","Python allows you to write to a file in binary mode. \n","Binary data is not encoded as text, and using binary write mode  ensures that the file content is handled as raw bytes.\n"])
    file.seek(0)
    data=file.read()
    
    print(data)
print("=================================================")

#tuple

with open("demo.txt","w+") as file:
    file.writelines(("When dealing with non-text data (e.g., images, audio, or other binary data).\n","Python allows you to write to a file in binary mode. \n","Binary data is not encoded as text, and using binary write mode  ensures that the file content is handled as raw bytes.\n"))
    file.seek(0)
    data=file.read()
    print(data)
print("=================================================")

#set
with open("demo.txt","w+") as file:
    file.writelines({"When dealing with non-text data (e.g., images, audio, or other binary data).\n","Python allows you to write to a file in binary mode. \n","Binary data is not encoded as text, and using binary write mode  ensures that the file content is handled as raw bytes.\n"})
    file.seek(0)
    data=file.read()
    print(data)
print("=================================================")