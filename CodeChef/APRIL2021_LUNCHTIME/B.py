# cook your dish here
I = lambda:int(input())
In = lambda:list(map(int,input().split()))

mod = 10 ** 9 + 7
n = I()
A = In()
q = I()
Q = In()
ans = sum(A)
for i in range(q):
    ans = (ans * 2) % mod
    print(ans)
