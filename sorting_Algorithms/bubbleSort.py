def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
## main

arr=[2,3,5,6,1,2,6]
print(arr)
bubbleSort(arr)
print(arr)