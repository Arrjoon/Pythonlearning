# Python Program to Print all Prime numbers in an Interval
x = 2
y = 15
list = []
for i in range(x, y):
    if i == 1 or i == 0:
        continue
    else:
        for j in range(x, int(y/2)+1):
            if i % j == 0:
                break
            else:
                list.append(j)

print(list)
