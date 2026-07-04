# Last updated: 7/4/2026, 10:43:34 AM
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs():
            if len(s) == n:
                ans.append("".join(s))
                return
            if len(ans) >= k:
                return
            for c in "abc":
                if not s or s[-1] != c:
                    s.append(c)
                    dfs()
                    s.pop()

        ans = []
        s = []
        dfs()
        return "" if len(ans) < k else ans[k - 1]