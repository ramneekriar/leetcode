class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not char in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.isWord = True
    
    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if not char in cur.children:
                return False
            cur = cur.children[char]
        
        return cur.isWord
    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if not char in cur.children:
                return False
            cur = cur.children[char]
        
        return True
    
# Time = Each operation is O(n) where n in the length of given string/prefix
# Space = Total space is O(M) where m is the number of Trie nodes in the data structure