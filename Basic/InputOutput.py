'''
Printing Output using print() 
    -This function allows us to display text, variables and expressions on the console. 
'''
print("-------------------------print()--------------------------------------")
print("Hello world !")

'''
Output Formatting
1: Using Format()
'''
print("This is prince ${:.2f}".format(200))


'''
2: Using sep and end parameter

'''
print("Python is a ", end="good")# you can give anything you want to add at the end of the print..
print(" programming language");
# Seprating with Comma
print('A', 'J', sep='')

# for formatting a date
print('09', '12', '2016',sep='-')
# another example
print('Abhi121', 'gmail.com', sep='@')


'''
3: Using f-string

'''
print(f"Hii this is Abhinav Jaiswal.")# you an use variable inside the f-string directly by using {varibale_name} 

'''
4:Using % Operator
%d => integer
%f =>  float
%s =>  string
%x => hexadecimal
%o =>  octal

'''
int=5
float=10.5
string='This is string'

print("This is integer %d" %int)
print("This is float %f" %float)
print("%s" %string)



'''
Input function is use to take the user input in python ->input()
    - By default it take the string type value if you want to take other type you need to type cast.
    
1.Taking the single input 
'''
print("-------------------------input()----------------------------------")
#single input at a time 
name=input("Enter your Name:")
print(f"your Name is:{name}")

# multipale input at a time

id,name,age,dob=input("Enter Id,Name,Age and Dob :").split()
print(f'Id:{id}\nName:{name}\nAge:{age}\nDOB:{dob}')