class Solution:
    # your task is to complete this function
    # function should return an integer
    
    def func(self,string,sign):
        
        for ch in string:
            if not ("0"<=ch<="9"):return -1
        return sign*int(string)
    
    def atoi(self,string):
        if string and string[0]=='-':
            return self.func(string[1:],-1)
        return self.func(string,1)
