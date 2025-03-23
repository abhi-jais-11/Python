import time
import threading
def display():
    for _ in range(1001):
        print("Hello",end=" ")
        
def display_hello():
    for _ in range(1001):
        print("Hello",end=" ")
        
st=time.time()
t1=threading.Thread(target=display)
t1=threading.Thread(target=display_hello)
t1.start()
et=time.time()
print()
print("Total Time Taken By Thread Program:",(et-st)*1000)