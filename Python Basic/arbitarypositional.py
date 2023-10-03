def add(*num,**num1):
    sum=0
    for i in num:
        sum=sum+i
    print(f"sum is {sum}")
    print(num1)

add(3,4,5,7,a=12 ,name="arjun",cast="nepali")