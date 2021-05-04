class Solution:
    
    #Function to count the number of substrings that start and end with 1.
    def binarySubstring(self,n,s):
        cnt = s.count('1')
        return cnt*(cnt-1)//2
