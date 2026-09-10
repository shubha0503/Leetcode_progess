# Last updated: 9/10/2026, 1:52:21 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        m, n = len(s), len(t)
4        f = [[0] * (n + 1) for _ in range(m + 1)]
5        for i in range(m + 1):
6            f[i][0] = 1
7        for i, a in enumerate(s, 1):
8            for j, b in enumerate(t, 1):
9                f[i][j] = f[i - 1][j]
10                if a == b:
11                    f[i][j] += f[i - 1][j - 1]
12        return f[m][n]