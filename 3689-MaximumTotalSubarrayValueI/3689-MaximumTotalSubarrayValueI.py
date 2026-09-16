# Last updated: 9/16/2026, 11:50:42 AM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))