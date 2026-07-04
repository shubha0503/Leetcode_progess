# Last updated: 7/4/2026, 10:43:42 AM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {"a": -1, "b": -1, "c": -1}
        ans = 0
        for i, c in enumerate(s):
            d[c] = i
            ans += min(d["a"], d["b"], d["c"]) + 1
        return ans