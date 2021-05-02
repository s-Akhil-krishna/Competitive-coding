class Solution:
    def splitString(self, s: str) -> bool:
        pq = []
        n = len(s)
        st = ""
    
        for i in range(n):
            st += s[i]
            pq.append([int(st),i+1,1])
        # print(pq)
        while pq:
            num, idx,count = pq.pop()
            if idx == n and count>1:return True
            st = ""
            for j in range(idx,n):
                st += s[j]
                x = int(st)
                # print("!",num,x)
                if x == num-1:
                    j += 1
                    if x == 0:
                        while j<n and s[j] == '0':
                            j += 1
                    pq.append([x,j,count+1])
                    break
                if x > num - 1:
                    break
        return False
