'''

 3.Multilevel Inheritance: A class is derived from a class which is also derived from another class.

'''

class Base:
    def __init__(self):
        print("Base Class")


class Intermediate(Base):
    def __init__(self):
        print("Intermediate Class")

class Child(Intermediate):
    
    def __init__(self):
        print("Child Class")
        Intermediate.__init__(self)
        Base.__init__(self)
    
    
        


child=Child()
