def buyAndSell(arr):
    min_price=float ('inf')
    max_profit=0
    for i in range(len(arr)):
        if i<min_price:
            min_price=arr[i]
        elif i-min_price>max_profit:
            max_profit=arr[i]-min_price    

    return max_profit

## main

arr=[7,1,2,3,6,2]

print("max Profit : ",buyAndSell(arr))