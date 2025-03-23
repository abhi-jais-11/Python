class Student:
    
    avrage=None
    
    def __init__(self, *args, **kwargs) :
        self.name=kwargs.get('name')
        self.marks=kwargs.get('marks')
        
        Student.avrage=self.avrage(self.marks)
        print(id(self))
        
    @staticmethod
    def avrage(marks):
        return sum(marks)/len(marks)

    @staticmethod
    
    def get_grade():
        if Student.avrage >=90:
            return "A"
        elif Student.avrage >=80:
            return "B"
        elif Student.avrage >=70:
            return "C"
        elif Student.avrage >=60:
            return "C"
        else:
            return "F"


#object 
student=Student(name="Abhinav",marks=[80,90,90,90,90])
# print(id(Student))
print(id(student))
print(f"Name:{student.name} and Grade :{student.get_grade()}")
        
    

    

    
    