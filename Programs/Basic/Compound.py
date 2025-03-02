
#defining the function to calculate the compound interest

def Coumpund_Iterest(ammount,rate,time):
    
    return (ammount*(1+(rate/100))**time)-ammount







ammount=eval(input("Enter Ammount:"))
rate=eval(input("Enter Rate:"))
time=eval(input("Enter Time:"))

print(f"Compund Interest is:{Coumpund_Iterest(ammount,rate,time)}")

