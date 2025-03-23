class Const:
    
    def __init__(self):
      print("Hello World !")


class SubCons(Const):   
    def __init__(self ):
        print("Hello Sub !")
    
    def sub(self):
        super().__init__()
        print("Hello Sub !")

obj=SubCons()
obj.sub()
    