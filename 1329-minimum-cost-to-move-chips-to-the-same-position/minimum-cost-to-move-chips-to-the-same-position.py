class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even, odd = 0, 0
        for num in position:
            if num%2:
                odd += 1
            else:
                even += 1
        return min(odd, even)