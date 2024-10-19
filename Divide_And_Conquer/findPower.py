def solve(a,n):
    if n==0:
        return 1
    if n==1:
        return a
    else:
        mid=n//2
        b=solve(a,mid)
        res=b*b
        if n%2==0:
            return res
        else:
            return res*a
def findPower(a,n):
    if n<0:
        b=solve(a,n*-1)
        return 1/b     
    return solve(a,n)

# main 

print(findPower(2,-2))  #answer will be 0.25