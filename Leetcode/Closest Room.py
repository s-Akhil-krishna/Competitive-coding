from sortedcontainers import SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        events = []
        
        for i,sz in rooms:
            events.append((-sz,0,i,-1))
        
        for i,(p,sz) in enumerate(queries):
            events.append((-sz,1,p,i))
        
        events.sort()
        sl = SortedList()
        res = [-1] * len(queries)
        
        for sz, t, p, d in events:
            if t == 0:
                sl.add(p)
                continue
            
            ans = -1
            index = sl.bisect_left(p)
            if 0 <= index < len(sl):
                ans = sl[index]
            
            index -= 1
            if 0 <= index < len(sl):
                if abs(p-sl[index]) <= abs(p-ans):
                    ans = sl[index]
            
            res[d] = ans
        return res
                
        
