# Last updated: 7/18/2026, 1:12:08 PM
1class Solution:
2    def findGCD(self, nums: List[int]) -> int:
3        return gcd(max(nums), min(nums))