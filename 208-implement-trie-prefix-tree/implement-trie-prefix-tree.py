class TrieNode:

    def __init__(self):
        self.links = [None] * 26
        self.flag = False 
        
    def contains_key(self, key):
        return self.links[ord(key) - ord('a')] != None

    def get(self, key):
        return self.links[ord(key) - ord('a')]

    def put(self, key, node):
        self.links[ord(key) - ord('a')] = node

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not cur.contains_key(c):
                cur.put(c, TrieNode())
            cur = cur.get(c)
        cur.setEnd()

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not cur.contains_key(c):
                return False
            cur = cur.get(c)
        return cur.isEnd()

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not cur.contains_key(c):
                return False
            cur = cur.get(c)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)