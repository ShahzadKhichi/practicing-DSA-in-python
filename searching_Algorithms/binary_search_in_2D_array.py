def binearySearch(arr,target):
    m=len(arr)
    n=len(arr[0])
    s=0
    e=m*n-1
    while(s<=e):
        mid=s+(e-s)//2
        element=arr[mid//n][mid%n]
        if(element==target):
            return mid//n,mid%n
        elif(element>target):
            e=mid-1
        else:
            s=mid+1
    return -1,-1     

## main

arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]

print("position of element : ",binearySearch(arr,3))