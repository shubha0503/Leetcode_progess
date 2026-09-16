# Last updated: 9/16/2026, 11:57:14 AM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))