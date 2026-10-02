# Last updated: 10/2/2026, 10:49:34 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        def dfs(l: int, r: int, t: str):
4            if l > n or r > n or l < r:
5                return
6            if l == n and r == n:
7                ans.append(t)
8                return
9            dfs(l + 1, r, t + "(")
10            dfs(l, r + 1, t + ")")
11
12        ans = []
13        dfs(0, 0, "")
14        return ans