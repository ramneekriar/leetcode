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

# Array Implementation -> Maybe more appropriate for dense tries? I think there is caching with arrays

class TrieNode2:
    def __init__(self):
        self.children = [0]*26
        self.isWord = False

class Trie2:

    def __init__(self):
       self.root = TrieNode2()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            index = ord(char) - ord('a')
            if cur.children[index] == 0:
                cur.children[index] = TrieNode2()
            cur = cur.children[index]

        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            index = ord(char) - ord('a')
            if cur.children[index] == 0:
                return False
            cur = cur.children[index]
        
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if cur.children[index] == 0:
                return False
            cur = cur.children[index]
        
        return True
    
# Time = Each operation is O(n) where n in the length of given string/prefix
# Space = Total space is O(26) as 26 empty spaces will always be defined for every node