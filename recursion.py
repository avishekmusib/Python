#find factorial
def fact(n):
    ans=1
    if n==0:
        return ans
    else:
        ans *= fact(n-1)
        return n*ans
print(fact(5))
#find recurtion


