# y = m * x +c a inear equtation

def outer_function(m):
    x=7#hard coded value
    def inner_function(c):
       return m*x +c
    return inner_function

if __name__=='__main__':
    closure = outer_function(3)
    print(closure)
    y=closure(2)
    print(y)