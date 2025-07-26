class Computer:
    def __init__(self):
        self.cpu = "i7"
        self.ram = 16

    def show(self):
        print(self.cpu , " : ", self.ram)



comp1 = Computer()
comp2 = Computer()
comp2.cpu = 'i9'

comp2.show()