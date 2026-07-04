# Last updated: 7/4/2026, 10:43:01 AM
class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i - 1] > x for i, x in enumerate(nums)) <= 1