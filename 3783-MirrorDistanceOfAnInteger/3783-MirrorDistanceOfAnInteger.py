# Last updated: 9/16/2026, 11:49:43 AM
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))