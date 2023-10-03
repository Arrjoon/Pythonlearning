# python function program

class employe:
    def takeInformation(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __init__(self, father_name):
        self.father = father_name

    def showInformation(self):
        print("The name of employe is ", self.name)
        print("The age of employe is ", self.age)
        print("The address of employe is "+self.address)
        print("Father name of the employee is :", self.father)


arjun = employe("Ram bhadur")
arjun.takeInformation("Arjun", 21, "Dhading ")
arjun.showInformation()
