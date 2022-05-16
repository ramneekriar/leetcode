class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = {}
        
        # adding freq of all nums in hash_map
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        output = []
        # building output list and removing it from hash_map once appended
        while len(output) != k:
            max_freq = max(hash_map, key= lambda x: hash_map[x])
            output.append(max_freq)
            hash_map.pop(max_freq)
            
        return output