from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / mid)
            
            if hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res

            
