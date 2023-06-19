class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

pers = Person('Swaroop')

# This short example can also be written as Person('Swaroop').say_hi()
pers.say_hi()

# This short example can also be written as Person('Swaroop').say_hi()
Person('Swaroop').say_hi()

for i in range(1, 10):
    print(i)
