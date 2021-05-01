# cook your dish here

I = lambda : int(input())
In = lambda : list(map(int,input().split()))

from math import gcd
n = I() 
res =[]
p = 1
for i in range(1,n):
    if gcd(i,n) == 1:
        p = p * i % n
        res.append(i)
if p == 1:
    print(len(res))
    print(*res)
else:
    ans = []
    for x in res:
        if x == p:continue
        ans.append(x)
    print(len(ans))
    print(*ans)
