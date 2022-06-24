class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        final_list = []
        hash_map = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hash_map:
                hash_map[sorted_word] = [word]
            else:
                hash_map[sorted_word].append(word)
        
        for group in hash_map:
            final_list.append(hash_map[group])
        
        return final_list