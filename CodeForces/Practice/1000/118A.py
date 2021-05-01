# cook your dish here
I = lambda : int(input())
In = lambda : list(map(int,input().split()))

x = input()
vow = "aeiouy"
x = x.lower()
s = ""
for ch in x:
    if ch not in vow:
        s += "." + ch 
print(s)