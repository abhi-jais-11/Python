'''
There are the 2way to create thred in python .

    1.importing  threading module 
    2.inheritting tread class

'''

#1st way
from threading import Thread,current_thread

#display function

def display(n,m):
    print(current_thread())
    for _ in range(n):
        print("Hello")
    print("-----------------------")
    for _ in range(m):
        print("Welcom")


#creating thred  object 
n=5

thread=Thread(target=display,args=(n,),kwargs={'m':5})
#thread start
thread.start()

print('-----------------------------')
print(current_thread())