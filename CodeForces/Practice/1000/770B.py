# cook your dish here
I = lambda : int(input())

n = I()

a = str(n)
ans = n
total =  sum(map(int,str(n)))

l = len(a)
cand = ['9']*l

for i in range(l):
    if a[i]!='0':
        cand[i] = str(int(a[i])-1)
        ctotal = sum(map(int,cand))
        if total < ctotal:
            cans = int("".join(cand))
            if cans <= n:
                total = ctotal
                ans = cans
        cand[i] = '9'
print(ans)