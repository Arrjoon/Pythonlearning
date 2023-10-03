'''
destructur are called when an objects gets destroyed. In python, destructures are not needed
as much as in c++ because Python has a garbage collector
that handles memory management automatically.

The __del__() methon is a known as a destructor method in python.
it is called when all refrences to the object have been deeted i.e. when 
an object is grabage collected.

syntax of destructor declaraton:
def __del__(self):
  # body of destructor

Note : A reference to objects is also deleted when the object goes out of reference or when the program ends. 


'''
