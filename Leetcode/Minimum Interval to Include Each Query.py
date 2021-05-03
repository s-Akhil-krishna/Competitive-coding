from sortedcontainers import SortedList
class Solution:
    def minInterval(self, intervals,queries):
        
        sl = SortedList()
        for i,q in enumerate(queries):
            sl.add([q,i])
        
        #sort intervals based on their size
        intervals.sort(key = lambda x:x[1]-x[0])
        
        ans = [-1]*len(queries)
        
        for s,e in intervals:
            left = sl.bisect_left([s,0])
            right = sl.bisect_left([e+1,0])
            delete = []
            for i in range(left,right):
                if i < len(sl):
                    if s <= sl[i][0] <= e:
                        ans[sl[i][1]] = e - s + 1
                        delete.append(sl[i])
            
            for x in delete:
                sl.remove(x)
        
        return ans
