# cook your dish here

I = lambda : int(input())
In = lambda : list(map(int,input().split()))

s = input()

j = -1
res = "YES"
for x in "hello":
    j = s.find(x,j+1)
    if j == -1:
        res ="NO"
print(res)