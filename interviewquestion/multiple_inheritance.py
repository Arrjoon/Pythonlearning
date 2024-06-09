class Base1:
    def __init__(self):
        self.str1="Base1"
        print("Base1")
    
    def base1_method(self):
        print("Method from Base1")

    
class Base2:
    def __init__(self):
        self.str2="Base2"
        print("Base2")

    def base2_method(self):
        print("Method from Base2")
    

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("Derived")
    
    
    def print_strs(self):
        print(self.str1,self.str2)

obj = Derived()

obj.print_strs()


