class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        marr = [0]*m
        narr = [0]*n
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for r, c in indices:
            marr[r] += 1
            narr[c] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if (marr[i] + narr[j])%2 == 1:
                    count += 1

        return count