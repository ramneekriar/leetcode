class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        if len(nums) < 3:
            return []
        
        sol = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                totalSum = a + nums[left] + nums[right]

                if totalSum > 0:
                    right -= 1
                elif totalSum < 0:
                    left += 1
                else:
                    sol.append([a, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[right]:
                        left += 1