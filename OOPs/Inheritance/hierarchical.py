'''
4.Hierarchical Inheritance: Multiple classes inherit from a single parent class.

'''

class Base:
    def __init__(self):
        print("Base Class")


class Intermediate(Base):
    def __init__(self):
        print("Intermediate Class")
        Base.__init__(self)

class Child(Base):
    
    def __init__(self):
        print("Child Class")
        Base.__init__(self)
    
    
inter=Intermediate()
child=Child()
