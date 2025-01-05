class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list:
        count = {} # hashmap of value : freq
        freq = [ [] for i in range(len(nums) + 1)] # to account for 0 value

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Time = O(n), Space = O(n)
# * Even though there is a double for loop, we are still accessing each element only once in the worse case scenario