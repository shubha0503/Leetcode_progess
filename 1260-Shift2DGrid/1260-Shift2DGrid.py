# Last updated: 7/30/2026, 12:49:43 AM
1class Solution:
2    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        m, n = len(grid), len(grid[0])
4        ans = [[0] * n for _ in range(m)]
5        for i, row in enumerate(grid):
6            for j, v in enumerate(row):
7                x, y = divmod((i * n + j + k) % (m * n), n)
8                ans[x][y] = v
9        return ans