class addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number  = " + str(self.first))
        print("second number  = " + str(self.second))
        print("Addition of two number =" + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# creating object of the class
# This will invoke parameterized constructor
obj = addition(100, 200)
# perform Additon
obj.calculate()
# display result
obj.display()
