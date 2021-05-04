def spaceString(str):
    # abc a bc ab c a b c
    n = len(str)
    res = []
    def dp(st,i):
        if i == n-1:
            res.append(st+str[i])
            return 
            
        dp(st+str[i],i+1)
        dp(st+str[i]+" ",i+1)
    
    dp("",0)
    return res
