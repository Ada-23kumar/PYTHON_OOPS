# Duck Typing

class VSCode:
    def execute(self):
        print("Compile")
        print("Run")


class Laptop:

    def Code(self, ide):
        print("Coding..")
        ide.execute()


lap1 = Laptop()

ide = VSCode()

lap1.Code(ide)