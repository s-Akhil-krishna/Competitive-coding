# cook your dish here
I = lambda:int(input())
In = lambda:list(map(int,input().split()))

from collections import Counter
T = I()
for _ in range(T):
    ans = "NO"
    N,W,Wr = In()
    ws = In()
    W -= Wr
    count = Counter(ws)
    for x in count:
        if count[x] > 1:
            pairs = count[x]//2
            W -= pairs*2*x
    if W <= 0:
        ans = "YES"
    print(ans)
