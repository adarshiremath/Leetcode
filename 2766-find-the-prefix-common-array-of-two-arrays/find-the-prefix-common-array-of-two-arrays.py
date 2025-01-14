class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        dit = {}
        count = 0
        for i, j in zip(A, B):
            dit[i] = dit.get(i, 0) + 1
            dit[j] = dit.get(j, 0) + 1

            if dit[i] >= 2:
                count += 1
            if i != j and dit[j] >= 2:
                count += 1
            res.append(count)
        return res