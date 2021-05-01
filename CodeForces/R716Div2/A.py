# cook your dish here

I = lambda : int(input())
In = lambda : list(map(int,input().split()))

t = I()
for _ in range(t):
    n = I()
    A = In()
    def ps(x):
        i = 1
        while i*i < x:
            i += 1
        if i*i == x:
            return True
        return False
        
    res = "NO"
    for x in A:
        if  not ps(x):
            res = "YES"
            break
    print(res)
            
