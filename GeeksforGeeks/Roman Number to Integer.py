def romanToDecimal(str):
    rms = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    nms = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    mp = {rms[i]:nms[i] for i in range(13)}
    n = len(str)
    ans = 0
    i = 0
    while i < n:
        if i+1<n and mp[str[i]] < mp[str[i+1]]:
            ans += mp[str[i+1]] - mp[str[i]]
            i += 2
        else:
            ans += mp[str[i]]
            i += 1
    return ans
