# Last updated: 11/25/2026, 7:51:51 PM
class Solution:
    def countValidSubstrings(self, s: str) -> int:
        left = 0
        result = 0
        last = -1
        for r in range(len(s)):
            if r >= 2 and s[r-2 : r+1] == "abc":
                last = r -2
                left = max(left,last+1)
            result += r -left +1
        return result