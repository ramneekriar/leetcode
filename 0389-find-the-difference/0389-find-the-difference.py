class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0

        for i in range(len(s)):
            res = res^ord(s[i])^ord(t[i])
        
        diffChar = chr(res^ord(t[-1]))
        return diffChar
    
# Time = 0(n), Space = O(1)