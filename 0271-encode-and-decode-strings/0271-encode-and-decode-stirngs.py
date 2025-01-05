class Solution:
    def encode(self, strs: list[str]) -> str:
        final_str = ""

        for word in strs:
            final_str += str(len(word)) + "#" + word
        
        return final_str

    def decode(self, s: str) -> list[str]:
        final_list = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            final_list.append(s[j + 1: j + length + 1])
            i = j + length + 1
        
        return final_list

# Time = O(n) Space = O(n)