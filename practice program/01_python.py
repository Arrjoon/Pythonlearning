# write a python program which will
#  kepp adding stream of number inputted
# by the user
sum = 0
while(True):
    userINput = input("Enter the price:")
    if(userINput != "q"):
        sum = sum + int(userINput)
    else:
        print(f"your bill total is {sum} ")
        print("Thanks for sopping with us!!")
        break
# receipt printer
