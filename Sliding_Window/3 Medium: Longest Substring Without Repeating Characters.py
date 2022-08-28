class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        else:
            left = 0
            right = 1
            max_len = 1
            substring = '' + s[left]

            while right < len(s):
                if s[right] not in substring:
                    substring = substring + s[right]
                else:
                    max_len = max(max_len, len(substring))
                    left += 1
                    right = left
                    substring = '' + s[left]

                right += 1
            
            max_len = max(max_len, len(substring))
            return max_len
    
    def lengthOfLongestSubstring_2(self, s: str) -> int: #faster solution
        charSet = set()
        left = 0
        res = 0
        
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right - left + 1)
        return res