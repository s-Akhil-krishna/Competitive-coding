from functools import lru_cache
class Solution:
    def largestPathValue(self, A , B):
        n = len(A)
        WHITE, GRAY, BLACK = 0, 1, 2
        vis = [0]*n
        graph = [[] for _ in range(n)]
        
        for u,v in B:
            graph[u].append(v)
            
        def cycle(node):
            if vis[node] == GRAY:
                return True
            
            vis[node] = GRAY
            for nei in graph[node]:
                if vis[nei] != BLACK:
                    if cycle(nei):return True
            vis[node] = BLACK
            return False
        
        for node in range(n):
            if vis[node] == WHITE:
                if cycle(node):return -1
        
        @lru_cache(None)
        def dfs(node,color):
            count = +(A[node] == color)
            res = 0
            for nei in graph[node]:
                res = max(res, dfs(nei, color))
            return res + count
                
                
        res = 0
        for node in range(n):
            res = max(res, dfs(node,A[node]))
        return res
        
