#Python program for implementation of selection
#sort
A=[64,23,13,44,11]

for i in range(len(A)-1):
    print(i)

    min_idx=i
    for j in range(i+1,len(A)):
        if A[min_idx]>A[j]:
            min_idx=j
    
    A[i],A[min_idx]=A[min_idx],A[i]

print("Sorted Array")
for i in range(len(A)):
    print(A[i],end=",")