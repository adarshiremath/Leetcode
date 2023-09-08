class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def factorial(i):
            if i == 0: return 1
            return i * factorial(i-1)
        res = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                row.append(factorial(i)//(factorial(j)*factorial(i-j)))
            res.append(row)
        return res
