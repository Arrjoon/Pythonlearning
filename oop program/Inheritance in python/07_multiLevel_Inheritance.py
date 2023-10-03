# when we have child and grand child relationship
class Base(object):
    # constructor
    def __init__(self, name):
        self.name = name
    # to get name

    def getName(self):
        return self.name

# Inherited or Sub class (note person in bracket)


class child(Base):
    # constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
    # to get name

    def getAge(self):
        return self.age

# Inherited or Sub class (note Person in bracket)


class Grandchild(child):
    # constructor
    def __init__(self, name, age, address):
        child.__init__(self, name, age)
        self.address = address

    def getAddress(self):
        return self.address


# Driver code
g = Grandchild("arjun", 21, "nepal")
print(g.getName(), g.getAge(), g.getAddress())
