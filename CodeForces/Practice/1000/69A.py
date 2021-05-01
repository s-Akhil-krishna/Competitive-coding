# cook your dish here
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

ans = [0,0,0]
n = I()
for _ in range(n):
    a,b,c = In()
    ans = [ans[0]+a,ans[1]+b,ans[2]+c]
res = "YES"
for x in ans:
    if x!=0:
        res = "NO"

print(res)
    