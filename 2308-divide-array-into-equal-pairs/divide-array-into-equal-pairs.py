class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dit = {}

        for i in nums:
            dit[i] = dit.get(i, 0) + 1
        

        for k, v  in dit.items():
            if v % 2 != 0:
                return False
        

        return True