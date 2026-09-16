# Last updated: 9/16/2026, 11:56:16 AM
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)