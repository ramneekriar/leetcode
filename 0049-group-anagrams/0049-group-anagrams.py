from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            sortedStr = ''.join(sorted(list(s)))
            hashmap[sortedStr].append(s)
        
        return list(hashmap.values())
    
# Time = O(m x n) (m = total number of input strings, n = avg len of string)
# Space = O(n)