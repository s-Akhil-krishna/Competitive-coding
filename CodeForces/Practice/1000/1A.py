# cook your dish here

I = lambda : int(input())
In = lambda : list(map(int,input().split()))

n,m,a = In()
print( ((n+a-1)//a) * ((m+a-1)//a) )