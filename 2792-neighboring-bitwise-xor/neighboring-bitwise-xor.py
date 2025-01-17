class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        Sum = 0
        for i in derived:
            Sum = Sum ^ i
        return False if Sum else True