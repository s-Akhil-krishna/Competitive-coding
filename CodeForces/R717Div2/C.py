# cook your dish here
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

import sys
from functools import lru_cache
from math import gcd
N = I()
arr = In()


x = sum(arr)
if x & 1:
    print(0)
    sys.exit()
y = x // 2

@lru_cache(None)
def dp(i,amt,y):
    if i == N:
        if amt == y:
            return True
        return False
    if arr[i] + amt <= y:
        return dp(i+1,amt+arr[i],y) or dp(i+1,amt,y)
    return dp(i+1,amt,y)
 
res = dp(0,0,y)
if res:
    flag = 0
    for i,x in enumerate(arr,1):
        if x&1:
            flag = 1
            print(1)
            print(i)
            break
    if flag == 0:
        print(1)
        ans = arr[0]
        for x in arr:
            ans = gcd(x,ans)
        for i,x in enumerate(arr,1):
            if (x // ans) & 1:
                print(i)
                break
else:
    print(0)
        

