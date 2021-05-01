# cook your dish here

from heapq import heapify,heappush,heappop
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

dp = [6,2,5,5,4,5,6,3,7,6]
pq = [(-1,2),(-2,5),(-3,5),(-4,4),(-5,5),(-6,6),(-7,3),(-8,7),(-9,6)]
n = I()
heapify(pq)
res = 1
while pq:
    cand,val = heappop(pq)
    cand = -cand
    # print(cand,val)
    if val > n:
        continue
    res = max(res,cand)
    for i in range(10):
        x = cand*10 + i
        v = val + dp[i]
        heappush(pq,(-x,v))
print(res)
