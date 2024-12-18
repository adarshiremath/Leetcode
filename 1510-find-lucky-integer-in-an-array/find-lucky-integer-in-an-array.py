class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dit = {}
        for i in arr:
            dit[i] = dit.get(i, 0) + 1
        Max = -1
        for k,v in dit.items():
            if k == v:
                if Max < k:
                    Max = k
        return Max