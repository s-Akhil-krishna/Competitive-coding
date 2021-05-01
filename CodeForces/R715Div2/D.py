
import sys
def I():return  int(sys.stdin.readline())
def In(): return map(int,sys.stdin.readline().split())
def S(): return sys.stdin.readline()
def main():

    def solve(a,b,n):
        i =0
        res = []
        while i< 2*n:
            if a[i] == b[i]:
                res.append(a[i])
            else:
                res.extend(['0','1'])
            i += 1
        if len(res) <= n * 3:
            return "".join(res)
        return -1
    t = I()         
    for _ in range(t):
        n= I()
        a = S()
        b = S()
        c = S()
        cand = solve(a,b,n)
        if isinstance(cand,str):
            print(cand)
            continue
        cand = solve(b,c,n)
        if isinstance(cand,str):
            print(cand)
            continue
        cand = solve(a,c,n)
        if isinstance(cand,str):
            print(cand)
            continue
        

if __name__ == '__main__':
    main()

