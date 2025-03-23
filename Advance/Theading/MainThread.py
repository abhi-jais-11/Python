'''
Threads are the python objects of the threading.Thread() class.

current_thread()-->rteurn the object of the current working thread.

'''

import threading 

#it will return the current working thred which is main thred
print(threading.current_thread()) # Main thred
print(threading.current_thread().ident) # return thread id 
print(threading.current_thread().name) #  return thread name
print(threading.current_thread()) # Main thred
print(threading.current_thread().is_alive()) #if thread start return true