import time

def display():
    for _ in range(1001):
        print("Hello",end=" ")
        
def display_hello():
    for _ in range(1001):
        print("Hello",end=" ")
        
st=time.time()
display()
display_hello()
et=time.time()
print()
print("Total Time Taken By Program:",(et-st)*1000)