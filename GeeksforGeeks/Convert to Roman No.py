def convertRoman(n):
    # 1 4 5 9 10 
    rms = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    nms = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    res = ""
    for i in range(12,-1,-1):
        while n >= nms[i]:
            res += rms[i]
            n -= nms[i]
    return res
