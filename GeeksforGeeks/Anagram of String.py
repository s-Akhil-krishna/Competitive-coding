from collections import Counter
def remAnagram(str1,str2):
    cnt1 = Counter(str1)
    cnt2 = Counter(str2)
    ans = 0
    for x in cnt1:
        if cnt1[x] > cnt2[x]:
            ans += cnt1[x] - cnt2[x]
    
    for x in cnt2:
        if cnt2[x] > cnt1[x]:
            ans += cnt2[x] - cnt1[x]
    
    return ans
