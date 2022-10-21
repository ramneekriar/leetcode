class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(' ')
        hash_map = {}
        
        if len(pattern) != len(words): return False
        if len(set(pattern)) != len(set(words)): return False
        
        for i in range(len(words)):
            if pattern[i] not in hash_map:
                hash_map[pattern[i]] = words[i]
            elif hash_map[pattern[i]] != words[i]:
                return False
        
        return True