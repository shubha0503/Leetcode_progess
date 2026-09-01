# Last updated: 9/1/2026, 11:10:59 AM
1class Solution:
2    def stoneGameVIII(self, stones: List[int]) -> int:
3        @cache
4        def dfs(i: int) -> int:
5            if i >= len(stones) - 1:
6                return s[-1]
7            return max(dfs(i + 1), s[i] - dfs(i + 1))
8
9        s = list(accumulate(stones))
10        return dfs(1)