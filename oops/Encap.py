# accesser and mutator
# getter and setter

class Person:

    def __init__(self):
        self.age = None

    def get_age(Self):
        return Self.age

    def set_age(self, age):
        self.age = age
        

p1 = Person()

p1.set_age(10)

print(p1.get_age())