# Last updated: 7/4/2026, 10:42:40 AM
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)