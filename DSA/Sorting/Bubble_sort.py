def bubbleSort(arr):
    n=len(arr)

    #For loop to traverse through all
    #element in an array

    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


if __name__== "__main__":
    arr=[3,4,2,45,23,9]

    bubbleSort(arr)

    for i in range(len(arr)):
        print(arr[i])