class CSStudent:
    name = None
    stream = 'cse'  # class variable

    def __init__(self, name, roll):
        self.name = name  # instance variable
        self.roll = roll  # instance variable


a = CSStudent("arjun", 1)
b = CSStudent("menuka", 2)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)
print(CSStudent.stream)
# if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream)
