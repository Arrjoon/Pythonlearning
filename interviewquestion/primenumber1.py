from math import sqrt
num = int(input("Enter to check prime number"))

for i in range(2, int(sqrt(num))+1):
    if num % i == 0:
        print("ts no t prime number")
    else:
        print("Its prime number")
