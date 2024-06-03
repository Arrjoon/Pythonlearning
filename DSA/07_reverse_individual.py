#Python3 program to reverse individual words


def reverseWords(string):
    #Traverse given string and push all characters

    stack=[]
    for i in range(len(string)):
        if string[i] != " ":
            stack.append(string[i])
        else:
            while len(stack)>0:
                print(stack[-1],end="")
                stack.pop()
            print("",end=" ")
    while len(stack)>0:
        print(stack[-1],end="")
        stack.pop()

    # print(stack)


reverseWords("My name is arjun nepali")