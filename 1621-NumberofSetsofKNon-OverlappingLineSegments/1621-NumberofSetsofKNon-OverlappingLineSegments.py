# Last updated: 9/16/2026, 11:27:05 PM
1class Solution:
2    def numberOfSets(self, n: int, k: int) -> int:
3        mod = 10**9 + 7
4        f = [[0] * (k + 1) for _ in range(n + 1)]
5        g = [[0] * (k + 1) for _ in range(n + 1)]
6        f[1][0] = 1
7        for i in range(2, n + 1):
8            for j in range(k + 1):
9                f[i][j] = (f[i - 1][j] + g[i - 1][j]) % mod
10                g[i][j] = g[i - 1][j]
11                if j:
12                    g[i][j] += f[i - 1][j - 1] + g[i - 1][j - 1]
13                    g[i][j] %= mod
14        return (f[n][k] + g[n][k]) % mod