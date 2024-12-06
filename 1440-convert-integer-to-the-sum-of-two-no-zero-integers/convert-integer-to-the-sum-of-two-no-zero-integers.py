class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isNonZeroInt(n: int) -> bool:
            if '0' in list(str(n)):
                return False
            return True
        
        for i in range(1, n):
            if isNonZeroInt(i) and isNonZeroInt(n - i):
                return [i, n-i]