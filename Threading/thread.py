'''

Way To Create Thread:

    1.Without using any class.
    2.By using class.

'''

'''
Method:

    1. getName #return thread name or [thread.name]
    2. setName() #use to set thread name 
    3. current_thread() #return current thred object
    4. ident #return the id of the thread.
    5. active_count() #return the all active thread
    6. enumrated() #return the all active thred information about the thread.
    7. isAlive() #return is thread alive or not.
    8. join() #use to wait to one complet their task.
    9. Daemon Thread --> which executing inside background called daemon thread.
    10. isDaemon() or daemon # return if thread daemon 
    11. setDaemon(True) #change the nature of daemon before starting only .
    
    
Synchronization:
----------------
'''


from threading import *
import time

def wish(name):
    for i in range(1,11):
       print("Hello Welcome ",end=" ")
       time.sleep(2)
       print(name)


    
thread=Thread(target=wish,args=("Jack",))
# thread.start()
# thread.join()
print('------------------------------------')

print("Current Thread Is: ",current_thread())
print("Id of thread :",thread.ident)
print("Is Alive :",thread.is_alive())
print("Active Count:",active_count())
print("Active Count Information:",enumerate())
print("Is Daemon:",thread.isDaemon)


print('------------------------------------')

