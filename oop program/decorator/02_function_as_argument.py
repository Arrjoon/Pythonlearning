def shout(text):
    return text.upper()

def wishper(text):
    return text.lower()

def greet(func):
    greeting = func("""Hi,I am arjun nepali i live in class 12""")
    print(greeting)

greet(shout)
greet(wishper)