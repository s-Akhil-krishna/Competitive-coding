# cook your dish here

I = lambda : int(input())
In = lambda : list(map(int,input().split()))

t = I()
for _ in range(t):
    n,k = In()
    A = In()
    op = 0
    j = 0
    while j < n and op!=k:
        if A[j] == 0: j += 1
        else:
            A[j] -= 1
            A[-1] += 1
            op += 1
        
    print(*A)