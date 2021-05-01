# cook your dish here
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

t = I()
for _ in range(t):
    n = I()
    A = In()
    pre = [0]
    for x in A:
        pre.append(pre[-1]^x)
    
    res = "NO"
    for i in range(1,n):
        a = pre[i]
        b = pre[i] ^ pre[n]
        if a == b:
            res = "YES"
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            a = pre[i]
            b = pre[i] ^ pre[j]
            c = pre[j] ^ pre[n]
            if a == b == c:
                res = "YES"
    
    print(res)