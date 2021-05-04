def strstr(s,x):
    m,n = len(s),len(x)
    for i in range(m):
        if s[i] == x[0]:
            for j in range(n):
                if i+j>=m or s[i+j]!=x[j]:
                    break
                if j == n-1:
                    return i
    return -1
