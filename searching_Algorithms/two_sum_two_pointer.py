def targetSum(arr,target):
    left=0
    right=len(arr)-1
    while(left<right):
        sum=arr[left]+arr[right]
        if sum==target:
            return left,right
        elif sum>target:
            right-=1
        else:
            left+=1
    return -1,-1

##main

arr=[1,2,3,4,5,6]

print("target sum : " ,targetSum(arr,10))