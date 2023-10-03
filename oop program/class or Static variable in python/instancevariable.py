class Person:
    status = "Student"

    def __init__(self, name):
        self.name = name

    def setVariable(self, roll):
        self.rollno = roll

    def getVariable(self):
        return self.rollno


arjun = Person("arjun nepali")
print(arjun.name)
arjun.setVariable(190345)
print(arjun.getVariable())
