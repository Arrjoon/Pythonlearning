list =[1,2,3,4,22,343,22,33]
def function(list):   
    max = list[0]
    for i in list:
        if i>max:
            max=i
    return max
print(function(list))