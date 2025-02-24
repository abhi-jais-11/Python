'''
1. write a program to find the mont name using the month in number:

'''
months={
    1:"January",
    2:"Febuary",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
month=int(input("Enter the Month :"))
if month in months:
    print(f" Without Match Month is {months[month]}")
else:
    print("Invalid month:")

match month :
    case 1:
        print(f" With Match Month is January")
    case 2:
        print(f" With Match Month is Febuary")
    case 3:
        print(f" With Match Month is March")
    case 4:
        print(f" With Match Month is April")
    case 5:
        print(f" With Match Month is May")
    case 6:
        print(f" With Match Month is June")
    case 7:
        print(f" With Match Month is July")
    case 8:
        print(f" With Match Month is August")
    case 9:
        print(f" With Match Month is September")
    case 10:
        print(f" With Match Month is October")
    case 11:
        print(f" With Match Month is November")
    case 12:
        print(f" With Match Month is December")
    case _:
        print(f" With Match Invalid month:")
        