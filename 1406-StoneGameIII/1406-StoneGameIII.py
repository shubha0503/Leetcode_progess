# Last updated: 8/3/2026, 2:56:22 PM
1class Solution:
2    def stoneGameIII(self, stoneValue: List[int]) -> str:
3        @cache
4        def dfs(i: int) -> int:
5            if i >= len(stoneValue):
6                return 0
7            ans = -inf
8            s = 0
9            for j in range(i, i + 3):
10                if j >= len(stoneValue):
11                    break
12                s += stoneValue[j]
13                ans = max(ans, s - dfs(j + 1))
14            return ans
15
16        res = dfs(0)
17        if res == 0:
18            return 'Tie'
19        return 'Alice' if res > 0 else 'Bob'