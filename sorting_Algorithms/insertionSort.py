def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while (j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key



## main

arr=[4,5,2,1,5,3]
print("before sorting : ",arr)
insertionSort(arr)
print("after sorting  : ",arr)

