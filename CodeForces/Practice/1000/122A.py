# cook your dish here
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

n = I()
lucky = almost = "YES"
tmp = n
while tmp:
    rem = tmp % 10
    tmp //= 10
    if rem not in (7,4):
        lucky = almost = "NO"

cand = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
for x in cand:
    if n % x == 0:
        almost = "YES"
        
print(almost)
