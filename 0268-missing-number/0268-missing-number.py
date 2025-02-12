class Solution:
    def missingNumber_1(self, nums: list[int]) -> int:
        # Bitwise
        result = len(nums)
        for i, num in enumerate(nums):
            result = result ^ i ^ num
        
        return result
    
    def missingNumber_2(self, nums: list[int]) -> int:
        # Formula
        expected_sum = (len(nums)*(len(nums) + 1))//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Time = O(1), Space = O(1)