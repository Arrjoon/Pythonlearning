arr = [12,3,4,15]

enm =enumerate(arr)
print(enm)
t = 0
for i, val in enm:
    print(i)
    t +=val


print("this is value of t",t)