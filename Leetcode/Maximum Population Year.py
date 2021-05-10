class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = collections.Counter()
        for b,d in logs:
            for x in range(b,d):
                count[x] += 1
        res = float('inf')
        resCount = 0
        for x in count:
            if count[x] == resCount:
                res = min(res,x)
            elif count[x] > resCount:
                resCount = count[x]
                res = x
        return res
                
