class Solution:
    #https://en.wikipedia.org/wiki/Gray_code
    def func(self,prev):
        rev = prev[::-1]
        left = ['0'+x for x in prev]
        right = ['1'+x for x in rev]
        return left + right
    
    def generateCode(self, n):
        begin = ['0','1']
        for i in range(1,n):
            begin = self.func(begin)
        return begin
