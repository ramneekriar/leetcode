class Solution:
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