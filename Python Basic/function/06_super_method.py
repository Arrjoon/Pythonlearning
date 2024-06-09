class Parent:
    def __init__(self):
        print("My name is arjun nepali")

    def parent_mesage(self,message):
        print("This is parent function",message)
    

class Child(Parent):
    def __init__(self):
        pass
    

# x=Parent("Hello , and welcome!")
x=Child()
x.parent_mesage("my name")
# x.parent_mesage()