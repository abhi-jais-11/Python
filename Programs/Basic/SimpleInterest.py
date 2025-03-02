
def SimpleInterest(ammount,rate,time):
    return (ammount*rate*time)/100


ammount=eval(input("Enter Ammount:"))
rate=eval(input("Enter Rate :"))
time=eval(input("Enter Time:"))

print(f"Simple Interest Is :{SimpleInterest(ammount,rate,time)}")