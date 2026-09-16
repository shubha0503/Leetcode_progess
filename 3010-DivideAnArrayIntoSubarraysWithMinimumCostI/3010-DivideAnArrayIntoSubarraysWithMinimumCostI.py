# Last updated: 9/16/2026, 11:54:08 AM
class Solution:
    def minimumCost(self, nums):
        nums_rest = nums[1:]
        nums_rest.sort()
        return nums[0] + nums_rest[0] + nums_rest[1]