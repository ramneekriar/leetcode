class Solution:
    def longestConsecutive(nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
    def longestConsecutive_2(nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums_sorted = sorted(nums)
        max_length = 1
        length = 1
        
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i-1]:
                continue
            elif nums_sorted[i] == (nums_sorted[i-1] + 1):
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
        
        max_length = max(max_length, length)
        return max_length