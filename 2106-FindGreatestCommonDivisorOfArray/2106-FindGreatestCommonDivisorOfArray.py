# Last updated: 8/2/2026, 11:17:26 AM
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums), min(nums))