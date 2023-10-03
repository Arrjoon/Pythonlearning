# parent class
class person(object):
    # __init__ is know as a constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    # child class


class Employee(person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # invoking the __init__ of the parent class
        person.__init__(self, name, idnumber)


a = Employee("Rahul", 89999, 20000, "intern")
a.display()
