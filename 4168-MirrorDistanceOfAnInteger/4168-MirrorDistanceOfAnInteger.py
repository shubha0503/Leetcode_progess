# Last updated: 7/4/2026, 10:40:05 AM
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))