class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dit = {}
        
        for i in arr:
            dit[i]  = sum([int(bi) for bi in list(bin(i)[2:])])
        return sorted(arr, key = lambda x: (dit[x], x))