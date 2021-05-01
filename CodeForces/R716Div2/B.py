I = lambda : int(input())
In = lambda : list(map(int,input().split()))
 
t = I()
for _ in range(t):
    n,k = In()        
    mod = 10**9 + 7
    ans = n ** k 
    print(ans%mod)
