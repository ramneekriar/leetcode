class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]: # so far everything from left to mid is sorted in ascending order
                if target > nums[mid]:
                    left = mid + 1
                else:
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    if target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1
        
        return -1 

# Time = O(log n), Space = O(1)