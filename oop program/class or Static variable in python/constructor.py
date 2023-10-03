# Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name1 = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name1)


p = Person('Nikhil')
p.say_hi()
