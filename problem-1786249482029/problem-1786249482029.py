# Last updated: 8/9/2026, 9:54:42 AM
1class Solution:
2    def stoneGameII(self, piles: List[int]) -> int:
3        @cache
4        def dfs(i, m):
5            if m * 2 >= n - i:
6                return s[n] - s[i]
7            return max(
8                s[n] - s[i] - dfs(i + x, max(m, x)) for x in range(1, m << 1 | 1)
9            )
10
11        n = len(piles)
12        s = list(accumulate(piles, initial=0))
13        return dfs(0, 1)