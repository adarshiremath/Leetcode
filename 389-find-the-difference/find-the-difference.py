class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dit = {}
        for i in s:
            dit[i] = dit.get(i, 0) + 1
        print(dit)
        for i in t:
            if i in dit and dit[i] > 0:
                dit[i] = dit[i] - 1
            else:
                return i
        