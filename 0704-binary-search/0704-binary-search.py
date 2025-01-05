class Solution:
    def binarySearch_Iterative(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def binarySearch_Recursive(self, nums: list[int], target: int) -> int:
        def binarySearch(nums: list[int], left: int, right: int, target: int) -> int:
            if left > right:
                return -1
            
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return binarySearch(nums, left, mid - 1, target)
            else:
                return binarySearch(nums, mid + 1, right, target)

        return binarySearch(nums, 0, len(nums) - 1, target)

        