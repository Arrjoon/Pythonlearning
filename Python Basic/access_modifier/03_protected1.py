class Student:
    # _name = None
    # _roll =None
    # _branch=None
    #constructor

    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch

    def _displayRollAndBranch(self):

        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


arjun=Student("arjun",1232,"Kalimati")
arjun._displayRollAndBranch()