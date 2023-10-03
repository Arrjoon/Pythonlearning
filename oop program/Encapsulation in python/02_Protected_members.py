# Python program to
# demonstrate protected members

# creating a base class

class Base:
    def __init__(self):
        # protected member
        self._a = 2
# creating a derived class


class Derived(Base):
    def __init__(self):
        # calling constructor of base
        # class
        Base.__init__(self)
        print("Calling protected member of base class:", self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# can be Accessed but should not be done due to convention
print("Accessing protected member of obj1:", obj1._a)
# Accessing the protected variable outside
print("Accessing protected member of obj2:", obj2._a)
