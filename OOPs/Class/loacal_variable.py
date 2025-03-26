'''
Local Variable or Method Level Variable:
    -Local Variable directly define inside the method without any arguments/keywords.
    -They can only assiable inside the method.

'''
#example

class Calculater:
    
    @staticmethod
    def add(a,b):
        sum=a+b #sum and a,b are the local variable
        print(f"Sum :{sum}") 
    # print(a,b) #NameError: name 'a' is not defined


#object 

calc=Calculater()
calc.add(10,20)