class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        c = 0

        for i in range(len(grid)):
            res1 = -1
            res2 = -1

            for j in range(len(grid)):
                if grid[i][j] == 0:
                    c += 1
                res1 = max(res1, grid[i][j])
                res2 = max(res2, grid[j][i])

            res += res1 + res2

        return res + len(grid) * len(grid) - c