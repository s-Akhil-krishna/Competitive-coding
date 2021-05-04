def encode(arr):
    ch,cnt = "",0
    res = ""
    for i,x in enumerate(arr):
        if ch!=x:
            res += ch+str(cnt)
            ch,cnt = x,1
        else:
            cnt += 1
            
    return res[1:] + ch + str(cnt)
