class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False
        
        # create hash_map 
        hash_map = {}

        # hold freq of chars in string s
        for letter in s:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1

        # decrement freq of chars in string t
        for letter in t:
            if letter in hash_map and hash_map[letter] != 0:
                hash_map[letter] -= 1
            else: #char in t does not exist in s, not anagram
                return False
        return True

    def isAnagram_2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)