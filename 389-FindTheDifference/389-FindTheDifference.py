# Last updated: 11/25/2026, 7:57:46 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
    
        