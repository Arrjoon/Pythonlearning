def f(x):
    return x**3-5*x-9


def bisection(x1, x2, e):
    condition = True
    while condition:
        global x3
        x3 = (x1+x2)/2
        if(f(x3)*f(x1) < 0):
            x2 = x3
        else:
            x1 = x3
        condition = abs(f(x3)) > e


x1 = float(input("Enter the first guesses:"))
x2 = float(input("Enter the second guess:"))
error = float(input("Enter the allowable error:"))

if(f(x1)*f(x2) > 0.0):
    print("Root doesn't lies inside the bracket")
else:
    bisection(x1, x2, error)

print(x3)
