class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dit = {'b':0, 'a':0, 'n':0, 'l':0, 'o':0}
        for i in text:
            if i in dit.keys():
                dit[i] += 1
        count = min(dit['b'], dit['a'], dit['n'], dit['l']//2, dit['o']//2)
        return count