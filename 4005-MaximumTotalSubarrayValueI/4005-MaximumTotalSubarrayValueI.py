# Last updated: 7/4/2026, 10:40:30 AM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))