class Solution:
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # O(n^2) solution, inefficient
        hash_map = {}
        output = []
        
        nums = [0,0]
        for i in range(len(nums)):
            hash_map[nums[i]] = nums[:i] + nums[i + 1:]
        
        for key,values in hash_map.items():
            output.append(multiply(values))
        
        return output
    

    def productExceptSelf_2(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)
        prefix = 1
        postfix = 1
        
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output
        
    
def multiply(nums):
        ans = 1;
        for num in nums:
            ans *= num
        return ans
