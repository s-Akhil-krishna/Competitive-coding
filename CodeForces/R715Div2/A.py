T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    ans = []
    for x in A:
        if x & 1:
            ans.insert(0,x)
        else:
            ans.append(x)
    print(*ans)
