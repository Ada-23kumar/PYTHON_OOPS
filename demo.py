class Student:
    
    school = "Ineuron"

    def __init__(self):
        self.marks = 10

    def get_marks(self): # instance method
        return self.marks
    
    @staticmethod
    def add(x, y):       # static method
        return x + y 
    
    @classmethod 
    def get_School(self):
        return self.school
    
    


s1 = Student()

print(s1.marks)
# print(Student.school)
# print(s1.get_school())
print(s1.get_School()) 

print(Student.add(3, 5))