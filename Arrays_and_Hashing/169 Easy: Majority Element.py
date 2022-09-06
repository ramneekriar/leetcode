class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        return max(dict, key= lambda x: dict[x])