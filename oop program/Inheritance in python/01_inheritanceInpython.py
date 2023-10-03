class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


arjun = Person('arjun', 10)
arjun.display()
