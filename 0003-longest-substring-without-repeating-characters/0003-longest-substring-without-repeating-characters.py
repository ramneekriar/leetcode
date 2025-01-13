class Solution:
    
    def lengthofLongestSubstring(self, s: str) -> int:
        # empty string
        if len(s) == 0:
            return 0

        left = right = 0
        res = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        
        return res

    def lengthOfLongestSubstring_notOptimal(self, s: str) -> int:
        # empty string
        if len(s) == 0:
            return 0
        
        seen = set()
        ptr1 = 0
        ptr2 = 0
        res = 0

        while ptr2 < len(s):
            if s[ptr2] not in seen:
                seen.add(s[ptr2])
                ptr2 += 1
                res = max(res, (ptr2 - ptr1))
            else:
                res = max(res, (ptr2 - ptr1))
                ptr1 += 1
                ptr2 = ptr1
                seen.clear()
        
        return res

# Time = O(n^2) Space = O(n)