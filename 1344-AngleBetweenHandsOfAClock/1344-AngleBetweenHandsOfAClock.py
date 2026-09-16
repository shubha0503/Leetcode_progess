# Last updated: 9/16/2026, 11:58:39 AM
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = 30 * hour + 0.5 * minutes
        m = 6 * minutes
        diff = abs(h - m)
        return min(diff, 360 - diff)