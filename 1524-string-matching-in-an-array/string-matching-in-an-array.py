class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = list()
        words = sorted(words, key = lambda x: len(x))
        print(words)
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result