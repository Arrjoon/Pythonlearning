def binary_search(arr,target,low,high):
    if low<=high:
        mid=(low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            return binary_search(arr,target,mid+1,high)
        else:
            return binary_search(arr,target,low,mid-1)
    else:
        return -1

arr=[2,3,4,5,6,7]

target=6
result = binary_search(sorted(arr),target,0,len(arr)-1)

if result != -1:
    print(f"Binary Serach :Element found at index {result}")
else:
    print("Binary Search :Element not found ")