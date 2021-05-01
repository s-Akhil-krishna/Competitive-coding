import math,sys
from collections import defaultdict,deque
import bisect as bi
def yes():print('YES')
def no():print('NO')
def I():return (int(sys.stdin.readline()))
def In():return(map(int,sys.stdin.readline().split()))
def Sn():return sys.stdin.readline().strip()
def Pr(x): sys.stdout.write(str(x)+'\n')
# import functools
# sys.setrecursionlimit(15000)
def dict(a):
    d={} 
    for x in a:
        if d.get(x,-1)!=-1:
            d[x]+=1
        else:
            d[x]=1
    return d
 
#  Find leftmost value >= x #
def find_gte(a, x):
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i
    else:            
        return -1
 
def main():
    try:
        n=I()
        l=sorted(In())
        dp=[[0]*n for i in range(n)]
        for i in range(n-2,-1,-1):
            for j in range(i,n):
                dp[i][j]=l[j]-l[i]+min(dp[i+1][j],dp[i][j-1])
        print(dp[0][n-1])
    except:
        pass
        
M = 998244353
P = 1000000007
 
if __name__ == '__main__':
    # for _ in range(I()):main()
    for _ in range(1):main()
#End#
