# public Access modifier
#protected Access modifier
#private Access modifier

#program to illustrate public access modifier in a class

class Person:
    def __init__(self,name,age):
        self.P_name= name
        self.P_age=age

    def displayAge(self):
        print("Age:",self.P_age)


obj=Person("ARjun",23)
obj.displayAge()