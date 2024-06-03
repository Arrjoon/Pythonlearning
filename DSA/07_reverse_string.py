#How to Reverse a string using stack

def ReverseString(string):
    reverse_string =[]
    for char in string:
        reverse_string.append(char)
    
    return "".join(reversed(reverse_string))


a=ReverseString("My name is arjun")
print(a)
    