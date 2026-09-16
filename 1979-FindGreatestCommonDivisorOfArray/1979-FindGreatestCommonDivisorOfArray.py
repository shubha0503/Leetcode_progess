# Last updated: 9/16/2026, 11:56:13 AM
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums), min(nums))