# python program to demonstrate inheritance
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)

class person(object):
    # constructor
    def __init__(self, name):
        self.name = name
    # to get name

    def getName(self):
        return self.name
    # To check if the person is employee or not

    def isEmployee(self):
        return False
# Inherited or Subclass (Note person in bracket)


class Employee(person):
    # Here we return tue
    def isEmployee(self):
        return True
    # Driver code
    emp = person("Arjun")  # An object of the person
    print(emp.getName(), emp.isEmployee())


emp = Employee("hari")
print(emp.getName(), emp.isEmployee())
