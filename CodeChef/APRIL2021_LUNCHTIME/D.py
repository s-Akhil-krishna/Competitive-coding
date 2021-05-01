# cook your dish here
I = lambda:int(input())
In = lambda:list(map(int,input().split()))
from collections import defaultdict


T = I()
for _ in range(T):
    tree = defaultdict(lambda:[None])
    n,k,a = In()
    f = sorted(In())
    dist = {}
    for i in range(n-1):
        u,v = In()
        tree[u].append(v)
        if tree[v][0]==None:
            tree[v][0] = u
    
    def dfs(i,j):
        pi,pj = {},{}
        ans = 0
        if i==j:return 0
        ci,cj = i,j
        li,lj = 0,0
        while ci and cj:
            pi[ci]=li
            if ci in pj:
                return pi[ci] + pj[ci]
            ci = tree[ci][0]
            li += 1
            
            pj[cj]=lj
            if cj in pi:
                return pi[cj] + pj[cj]
                
            cj = tree[cj][0]
            lj+=1    

        while ci:
            pi[ci]=li
            if ci in pj:
                return pi[ci] + pj[ci]
            ci = tree[ci][0]
            li += 1
            
        while cj:
            pj[cj]=lj
            if cj in pi:
                return pi[cj] + pj[cj]
            cj = tree[cj][0]
            lj+=1      
    
    for i in range(1,n+1):
        for j in range(i,n+1):
            if (i,j) not in dist:
                dist[(i,j)] = dfs(i,j)
                #print("uvd",i,j,dist[(i,j)])
    au = []
    us = []
    for i in range(1,n+1):
        dopt,uopt = float('-inf'),None 
        for u in f:
            d = dist[min(a,u),max(a,u)] - dist[min(i,u),max(i,u)]
            #print("auiu",a,u,i,u,d)
            if d > dopt:
                dopt,uopt = d,u
        au.append(dopt)
        us.append(uopt)
    print(*au)
    print(*us)
        
