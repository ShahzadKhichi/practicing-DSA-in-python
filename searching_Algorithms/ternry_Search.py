def ternerySearch(arr,x):
    s=0
    e=len(arr)-1
    while s<=e:
        mid1=s+(e-s)//3
        mid2=e-(e-s)//3
        if arr[mid1]==x:
            return mid1
        if arr[mid2]==x:
            return mid2
        elif arr[mid1]>x:
            e=mid1-1
        elif arr[mid2]<x:
            s=mid2+1
        else:
            s=mid1+1
            e=mid2-1 
              
    return -1



## main 
arr=[1,2,3,4,4,5,5,5,5,5,6,7,7,8]
print("Index : ",ternerySearch(arr,1))
