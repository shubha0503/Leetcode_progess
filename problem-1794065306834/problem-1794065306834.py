# Last updated: 11/7/2026, 8:58:26 PM
1class Solution:
2    def countValidSubstrings(self, s: str) -> int:
3        left = 0
4        ans = 0
5        lasr = -1
6        for right in range(len(s)):
7            if right >= 2 and s[right-2:right+1] == "abc":
8                last = right -2
9                left = max(left,last+1)
10            ans += right -left +1
11        return ans