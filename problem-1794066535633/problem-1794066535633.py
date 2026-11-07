# Last updated: 11/7/2026, 9:18:55 PM
1class Solution:
2    def countValidSubstrings(self, s: str) -> int:
3        left = 0
4        result = 0
5        last = -1
6        for r in range(len(s)):
7            if r >= 2 and s[r-2 : r+1] == "abc":
8                last = r -2
9                left = max(left,last+1)
10            result += r -left +1
11        return result