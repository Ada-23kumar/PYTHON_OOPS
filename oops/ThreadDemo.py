from time import sleep
from threading import Thread

# class Hello:
class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(0.5)


# class Hi:
class Hi(Thread):
    def run(self):
        for i in range(500):
            print("hi")
            sleep(0.5)


obj1 = Hello()
obj2 = Hi()

# obj1.run()
# obj2.run()

obj1.start()
obj2.start()

