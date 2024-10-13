def binearySearch(arr,x):##Bineary Search function iterative
    s=0
    e=len(arr)-1
    while(s<=e):
        mid=s+(e-s)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            s=mid+1
        else:
            e=mid-1
    return -1
## main 
arr=[0,1,2,3,4,5,6,7,8]
x=8
print("Element present at index : ",binearySearch(arr,x))         
        
