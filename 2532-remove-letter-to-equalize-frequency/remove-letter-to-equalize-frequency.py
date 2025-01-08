class Solution:
    def equalFrequency(self, word: str) -> bool:
        dit = {}
        for i in word:
            dit[i] = dit.get(i, 0) + 1

        for i in range(len(word)):
            dit[word[i]] -= 1
            if dit[word[i]] == 0:
                del dit[word[i]]
            if len(set(dit.values())) == 1:
                return True
            dit[word[i]] = dit.get(word[i], 0) + 1
        
        return False