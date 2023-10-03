# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time

def funct():
    return f"my name is arjun"


def simpleGeneratorFun():
    yield 'hari'
    yield 'ram'
    yield funct()


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
