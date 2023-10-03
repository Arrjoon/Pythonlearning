class Father(object):
    fathername = ""

    def __init__(self, fathername):
        self.fathername = fathername

    def getFathername(self):
        return self.fathername


class Mother(object):
    mothername = ""

    def __init__(self, mothername):
        self.mothername = mothername

    # def getMothername(self):
    #     return self.mothername


class son(Father, Mother):
    sonname = ""

    def __init__(self, sonname, fathernam, mothername):
        Father.__init__(self, fathername=fathernam)
        Mother.__init__(self, mothername)
        self.sonname = sonname

    def displayAllname(self):
        print("Father name is "+self.fathername)
        print("Mother name is "+self.mothername)
        print("your name is "+self.sonname)


obj1 = son("abc", "hari", "gopal")
obj1.displayAllname()
