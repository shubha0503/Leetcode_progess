# Last updated: 8/2/2026, 11:25:39 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)