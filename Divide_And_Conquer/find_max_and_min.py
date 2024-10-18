def findMaxAndMin(arr,i,j):
    if i==j:
        return arr[i],arr[j]
    elif i==j-1:
        if arr[i]>arr[j]:
            return arr[i],arr[j]
        else:
            return arr[j],arr[i]
    else:
        mid=i+(j-i)//2
        max1,min1=findMaxAndMin(arr,i,mid)
        max2,min2=findMaxAndMin(arr,mid+1,j)
        max=0
        min=0
        if max1>max2:
            max=max1
        else:
            max=max2
        if min1<min2:
            min=min1
        else:
            min=min2
        return max,min    

## main fun()

arr=[1,2,3,4,5,2,23,45,2,34,6,2,4,6,7,2,0,-1,-1,-2]
print(findMaxAndMin(arr,0,len(arr)-1))## result will be (45,-2)           