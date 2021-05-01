import sys
def I():return  int(sys.stdin.readline())
def In(): return map(int,sys.stdin.readline().split())
def main():
    n= I()
    l = sorted(In())
    dp = [[0]*n for _ in range(n)]
    for i in range(n-2,-1,-1):
        for j in range(i,n):
            dp[i][j]=l[j]-l[i]+min(dp[i+1][j],dp[i][j-1])
    res =  dp[0][n-1]
    print(res)

if __name__ == '__main__':
    main()
