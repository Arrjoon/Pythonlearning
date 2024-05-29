def hello_decorator(func):
    #inner1 is a Wrapper function in 
    #which the argument is called

    def inner1():
        print("Hello,this is before function execution")

        func()

        print("This is after function execution ")

    return inner1

@hello_decorator
def function_to_be_used():
    print("This is inside function !!")

# function_to_be_used=hello_decorator(function_to_be_used)
function_to_be_used()