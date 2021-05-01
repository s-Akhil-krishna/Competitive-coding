# cook your dish here
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

n = I()
x = sorted(In())
q = I()
m = []
for i in range(q):
    m.append(I())

x.insert(0,0)

def query(m):
    lo,hi = 0,n
    while lo < hi:
        mi = lo + hi + 1 >> 1
        if x[mi] <= m:
            lo = mi 
        else:
            hi = mi - 1
    return lo 

res = list(map(query,m))
print(*res)
        