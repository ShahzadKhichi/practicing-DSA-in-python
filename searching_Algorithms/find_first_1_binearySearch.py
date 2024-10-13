def binearySearch(arr):
    s=0
    e=len(arr)-1
    result=-1
    while(s<=e):
        mid=s+(e-s)//2
        if(arr[mid]==1):
            result=mid
            e=mid-1
        else:
            s=mid+1   
    return result            


## main

arr=[0,0,0,0,0,0,0,1,1,1,1,1,1,1]
print("bad version : ",binearySearch(arr))
