# cook your dish here
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

t = I()
for _ in range(t):
    a = I()
    n = 2*a / (180-a) + 2
    if int(n) == n:
        print("YES")
    else:
        print("NO")