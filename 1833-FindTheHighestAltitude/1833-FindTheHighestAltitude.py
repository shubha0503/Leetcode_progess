# Last updated: 7/4/2026, 10:43:05 AM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))