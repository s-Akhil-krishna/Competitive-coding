class Solution:
    def isRotated(self,str1,str2):
        return str1[2:]+str1[:2] == str2 or str2[2:]+str2[:2]==str1
