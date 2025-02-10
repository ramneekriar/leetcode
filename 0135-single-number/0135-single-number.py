class Solution:
    def singleNumber(self, nums: list[int]):
        ans = 0
        for num in nums:
            ans ^= num
        
        return ans

# Time = O(n)
# Space = O(1)