import csv
import json

'''
Ther are the three way to read the file .

    -> using read() --> it read the entire file and return it 
    -> using readline() --> it read only single line of the file and return it
    -> using the readlines()--> it read all line of the file and return as a list.


'''

#using read.
print("------- --------With read()-----------------")
with open("demo.txt","r", encoding="utf-8") as file_read:
    text=file_read.read()
    print(text)
print('--------------------------------------------')
print()
#using readline
print("------- --------With readline()-----------------")
with open("demo.txt","r", encoding="utf-8") as file_readline:
    text=file_readline.readline()
    print(text)
print('--------------------------------------------')
print()
#using readlines
print("---------------With readline()-----------------")
with open("demo.txt","r", encoding="utf-8") as file_readlines:
    text=file_readlines.readlines()
    print(text)
print('--------------------------------------------')

#using the for loop
print("------- --------With readline()-----------------")
with open("demo.txt","r", encoding="utf-8") as file_readline:
    for i in file_readline:
        print(i)
print('--------------------------------------------')
print()


#while
with open("demo.txt","r", encoding="utf-8") as file_readline:
    line=file_readline.readline()
    while line:
        print(line.strip())
        line=file_readline.readline()
print('==================================')




#reading the json file and csv file 

with open("data.csv","r",  encoding="utf-8") as csv_file:
    data=csv.reader(csv_file)
    for i in data:
        print(i)
print("==============================================")

with open("data.json","r", encoding="utf-8") as json_file:
    data=json.load(json_file)
    print(data)