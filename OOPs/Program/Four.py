class Person:
    '''
    A simple class that override the object representaction.
    
    '''
    def __init__(self, *args, **kwargs):
        self.fname=kwargs.get('fname')
        self.lname=kwargs.get('lname')
    
    def __str__(self):
        return f"{self.fname} {self.lname}"


#objet creation
person=Person(fname="Jack",lname="Hunt")
print(person)