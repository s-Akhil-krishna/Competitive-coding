# cook your dish here


I = lambda : int(input())
In = lambda : list(map(int,input().split()))
from math import sqrt
T = I()
for _ in range(T):
    x,y = In()
    i = 1
    while i*i < x+y:
        i += 1
    ans = None
    if i*i != x+y:
        ans = "NO"
    else:
        ans = "YES"
        
    if i == 1:
        if x != 1:
            ans = "NO"
        else:
            ans = "YES"
    
        
    if ans == "NO":
        print("NO")
        continue
    
    n = int(sqrt(x+y))
    odd,even = n-1,1
    flag = 0
    while odd >= 1:
        odd_pairs = odd * even * 2
        if odd_pairs == y:
            flag = 1
            break
        odd -= 1
        even += 1
    ans = "YES" if flag==1 else "NO"
    
    if ans == "NO":
        print("NO")
        continue
    
    print(ans)
    print(n)
    for i in range(1,odd+1):
        print("1 " + str(i + 1) )
    for i in range(1,even):
        print("2 "+ str(odd + i + 1))
    
        
        
        