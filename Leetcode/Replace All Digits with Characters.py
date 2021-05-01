class Solution:
    def replaceDigits(self, s: str) -> str:
        return "".join(x if i&1==0 else chr(ord(s[i-1])+int(x)) for i,x in enumerate(s))
