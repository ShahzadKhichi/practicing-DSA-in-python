def LinearSearch(arr,x):
    for i in range(len(arr)):
        if(arr[i]==x):
            return i
    return -1        



arr=[23,53,3,5,2,45,12]
x=5
print("Element present at index : ",LinearSearch(arr,x))         
        
