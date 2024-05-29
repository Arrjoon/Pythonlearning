def func(fun):
    a=fun()
    return a

def greeting():
    print("hello")
    return "ab"
print(func(greeting))
