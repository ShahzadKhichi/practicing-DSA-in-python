def noOfWays(n):
    if n==0 or n==1:
        return 1
    else:
        return noOfWays(n-1)+ noOfWays(n-2)

# main

print(noOfWays(0))