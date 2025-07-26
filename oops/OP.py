a = 5
b = 6
c = "Adarsh"
d = "Kumar"

print(int.__add__(a, b))
print(str.__add__(c, d))

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self, other):
        total_m1 = self.m1 + other.m2
        # total_m2 = self.m2 + other.m2
        s3 = Student(total_m1)
        return s3
    
    def __str__(self):
        return str(self.m1) + " " + str (self.m2)


s1 = Student(45, 34)
# s2 = Student(99, 77)

s3 = s1.m1 + s1.m2  #Student.__add__(s1, s2)
                    # s1.__add__(s2)
print(s3)
