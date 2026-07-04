# Last updated: 7/4/2026, 10:45:36 AM
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)