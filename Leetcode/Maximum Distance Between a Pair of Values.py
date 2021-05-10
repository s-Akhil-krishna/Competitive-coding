class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        m,n = len(nums1),len(nums2)
        res = 0
        for i in range(m):
            #BinarySearch
            lo,hi = i,n-1
            while lo < hi:
                mi = lo + hi + 1 >> 1
                if nums2[mi] >= nums1[i]:
                    lo = mi
                else:
                    hi = mi - 1
            res = max(res,lo - i)
        return res
            
