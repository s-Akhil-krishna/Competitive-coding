class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        
        minleft = []
        stack = []
        for i,x in enumerate(nums):
            
            if not stack:
                minleft.append(0)
                stack.append((x,i))
                continue
            
            while stack and stack[-1][0] >= x:
                stack.pop()
            
            if stack:
                minleft.append(stack[-1][1] + 1)
            else:
                minleft.append(0)
            stack.append((x,i))
        
        stack = [] 
        minright = []
        for i in range(n-1,-1,-1):
            
            if not stack:
                minright.append(n-1)
                stack.append((nums[i],i))
                continue
            
            while stack and stack[-1][0] >= nums[i]:
                stack.pop()
            
            if stack:
                minright.append(stack[-1][1] - 1)
            else:
                minright.append(n-1)
            stack.append((nums[i],i))
            
        minright.reverse()
        res = max( nums[i]*(prefix[minright[i] + 1] - prefix[minleft[i]] ) for i in range(n))
        return res % mod
                
        
            
            
        
