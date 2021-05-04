def isValid(s):
    nums = s.split('.')
    if  len(nums)!=4:return 0
    for num in nums:
        if not 1 <= len(num) <= 3: return 0
        for ch in num:
            if not "0" <=  ch <= "9": return 0
        if not 0 <= int(num) <= 255:return 0
        dig = 1 if int(num)==0 else 0
        n = int(num)
        while n:
            dig += 1
            n //= 10
        if dig!=len(num):return 0
    return 1
