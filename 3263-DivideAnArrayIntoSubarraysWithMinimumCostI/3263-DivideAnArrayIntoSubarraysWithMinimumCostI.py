# Last updated: 7/4/2026, 10:41:45 AM
class Solution:
    def minimumCost(self, nums):
        nums_rest = nums[1:]
        nums_rest.sort()
        return nums[0] + nums_rest[0] + nums_rest[1]