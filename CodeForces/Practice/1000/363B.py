# cook your dish here
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

n,k = In()
A = In()
pre = [0]
for x in A:
    pre.append(pre[-1] + x)

ans = sum(A)
j = 0
for i,x in enumerate(pre):
    if i - k >= 0:
        cand =  x - pre[i-k]
        if cand < ans:
            ans = cand
            j = i-k

print(j+1)