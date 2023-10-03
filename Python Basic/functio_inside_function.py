def outerfuntion(show):
    print("I am a outer function",show())

def innerfunction():
    return "my name is arjun"

outerfuntion(innerfunction)