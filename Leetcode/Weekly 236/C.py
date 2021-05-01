class Solution:
    def minSideJumps(self, ob: List[int]) -> int:
        n = len(ob)        
        def func(state,point):
            if point==n-1:return min(state)
            l = ob[point+1] - 1
            newState = [float('inf')]*3
            for i in range(3):
                if i == l and l!=-1: continue
                else:
                    if state[i] != float('inf'):
                        newState[i] = state[i]
            for i in range(3):
                if state[i] == newState[i] == float('inf') and l!=i:
                    newState[i] = min(newState) + 1
            return func(tuple(newState),point+1)
        return func([1,0,1],0)
