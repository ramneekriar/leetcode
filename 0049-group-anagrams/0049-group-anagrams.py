from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            sortedStr = ''.join(sorted(list(s)))
            hashmap[sortedStr].append(s)
        
        return list(hashmap.values())
    
# Time = O(n * k log k) where n is the number of words and k is the average length of a word
# Space = O(n)

    def groupAnagrams_2(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            word = word.lower()
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            key = tuple(count)
            hashmap[key].append(word)
        
        return hashmap.values()

# Time: O(nk * 26) where n is the number of words and k is the number of letters in a word and 26 is constant but it's the letters we create everytime
# Space: O(nk)