class A:
    def __init__(self):
        self.m1 = 9
    


class X:
    def __init__(self):
        self.m3 = 10


class B(A, X):
    def __init__(self):
        super().__init__()
        self.m2 = 8


obj = B()


print(obj.m1)
print(obj.m3)
print(obj.m2)


