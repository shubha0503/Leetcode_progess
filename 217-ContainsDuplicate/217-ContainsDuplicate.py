# Last updated: 8/2/2026, 11:25:35 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        else:
            return True