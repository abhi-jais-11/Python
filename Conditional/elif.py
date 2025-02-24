'''
1.write a program to check number is positive or nigative or zero.

'''
num=eval(input("Enter the number :"))
if num>0:
    print(f"{num} is positive!")
elif num<0:
    print(f"{num} is negative!")
else:
    print(f"{num} is zero !")
    
    
'''
2. find the greatest among the three number 
'''
num1= eval(input("Enter the 1st number :"))
num2= eval(input("Enter the 2nd number :"))
num3= eval(input("Enter the 3rd number :"))
if num1 > num2 and num1 > num3 :
        print(f"{num1} is greater !")
elif num2> num3 :
    print(f"{num2} is greater !")
else:
    print(f"{num3 } is greater!")