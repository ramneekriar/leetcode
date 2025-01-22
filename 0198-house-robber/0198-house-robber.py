from functools import cache

class Solution:
    def rob(self, nums: list[int]) -> int:
        # Top Down Memoization
        cache = {}

        def dp(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            take = nums[i] + dp(i + 2)
            skip = dp(i + 1)
            result = max(take, skip)
            cache[i] = result
            return result
        
        return dp(0)

    def rob_cache(self, nums: list[int]) -> int:
        @cache
        def dp(i):
            if i >= len(nums):
                return 0
            take = nums[i] + dp(i + 2)
            skip = dp(i + 1)

            return max(take, skip)
        
        return dp(0)

# Time = O(n), Space = O(n)