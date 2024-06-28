def gen_fibonicaii_series(n):
    # a, b=0, 1
    # for _ in range(2,n):
    #     a, b = b, a+b
    # return b
    list = [0,1]
    a=0
    b=1
    for _ in range(2,n):
       a,b=b,a+b
    #    list.append(a)
       list.append(b)
    return list

print(gen_fibonicaii_series(5))


