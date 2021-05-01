# cook your dish here

# from functools import lru_cache
# @lru_cache(None)
# def dp(S,i,n,complete, started_t, started_tm):
#     if i == n: return complete*3 == n
#     if S[i] == 'T':
#         # a new seq started
#         # a seq ended 
#         cand = dp(S,i+1,n,complete,started_t+1,started_tm)
#         if started_tm:
#             cand |= dp(S,i+1,n,complete+1,started_t,started_tm-1)
#         return cand
#     else :
#         # if incomplete == 0: return False
#         if started_t == 0:return False
#         return dp (S,i+1,n,complete,started_t-1,started_tm+1)
        
def solve(S,n):
    left = right = 0 
    for ch in S:
        if ch == 'T':
            left += 1
        else:
            if left == 0:
                return False
            left -= 1

    for i in range(n-1,-1,-1):
        if S[i] == 'T':
            right += 1
        else:
            if right == 0:return False
            right -= 1 

    return S.count('M')*3 == n
            
        
        
T = int(input())
for t in range(T):
    N = int(input())
    S = input()
    res = solve(S,len(S))
    print("YES" if res else "NO")
