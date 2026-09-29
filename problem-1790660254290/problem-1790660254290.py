# Last updated: 9/29/2026, 11:07:34 AM
1class Solution:
2    def hasValidPath(self, grid: List[List[str]]) -> bool:
3        @cache
4        def dfs(i: int, j: int, k: int) -> bool:
5            d = 1 if grid[i][j] == "(" else -1
6            k += d
7            if k < 0 or k > m - i + n - j:
8                return False
9            if i == m - 1 and j == n - 1:
10                return k == 0
11            for a, b in pairwise((0, 1, 0)):
12                x, y = i + a, j + b
13                if 0 <= x < m and 0 <= y < n and dfs(x, y, k):
14                    return True
15            return False
16
17        m, n = len(grid), len(grid[0])
18        if (m + n - 1) % 2 or grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
19            return False
20        return dfs(0, 0, 0)