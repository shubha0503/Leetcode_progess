# Last updated: 7/4/2026, 10:46:20 AM
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return[seen[complement], i]
            seen[num] = i       