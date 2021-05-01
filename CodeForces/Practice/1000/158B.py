# cook your dish here
from collections import Counter
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

n = I()
s = In()
count = Counter(s)
car = 0

oneThree = min(count[1],count[3])
count[1] -= oneThree
count[3] -= oneThree
twoTwo = count[2] // 2
car = oneThree+twoTwo
count[2] -= twoTwo*2

oneTwo = min(count[1],count[2])
count[1] -= oneTwo
count[2] -= oneTwo

if count[1]:
    x = min(oneTwo,count[1])
    count[1] -= x
car += oneTwo 
    
if count[1] >0 :
    car += count[1] // 4 
    if count[1] % 4:
        car += 1
        
if count[2] >0:
    car += count[2]//2 + count[2]%2
if count[3]>0:
    car += count[3]
if count[4]>0:
    car += count[4]
print(car)
    