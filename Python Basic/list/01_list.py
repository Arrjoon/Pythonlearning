list1 = [1, 2, 3, 4]
print(list1)
a = list1[0]
list1[0] = list1[3]
list1[3] = a
print(list1)


def function(newlist):
    size = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = temp
    return newlist


list2 = [4, 3, 5, 6, 7]
a = function(list2)
print(a)
