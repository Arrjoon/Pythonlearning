# Python program to
# demonstrate private members

# Creating a Base class

class Base:
    def __init__(self):
        self.a = "Arjun Nepali"
        self.__c = "Rupak Nepali"
# Creating derived class


class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class:")
        print(self.__c)


# Deriver code
obj1 = Base()
print(obj1.a)
# obj2 = Derived()
# private member of the base class is called
# inside derived class
