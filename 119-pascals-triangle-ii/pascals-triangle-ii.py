class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def factorial(i):
            if i == 0: return 1
            return i * factorial(i-1)
        res = []
        i = rowIndex
        for j in range(rowIndex+1):
            res.append(factorial(i)//(factorial(j)*factorial(i-j)))
        return res