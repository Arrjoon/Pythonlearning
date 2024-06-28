#taking number of terms to print the series




def fibonicaaii():
    n=9
    first=0
    second=1
    series =[first,second]

    # if n==0:
    #     return series
    
    for i in range(n-2):
        sum=series[i]+series[i+1]
        series.append(sum)
        first = second
        second =sum
    
    return series

print(fibonicaaii())


# for i in range(4,1,-1):
#     print(i)

