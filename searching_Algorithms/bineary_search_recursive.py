def binearySearch(arr,x,s,e):##Bineary Search function recursive
    if s>e:
        return -1
    else:
        mid=s+(e-s)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
           return binearySearch(arr,x,s+1,e)
        else:
            return binearySearch(arr,x,s,e-1)

## main 
arr=[0,1,2,3,4,5,6,7]
x=5

print("Element present at index : ",binearySearch(arr,x,0,len(arr)-1))         
        
