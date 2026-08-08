# Last updated: 8/8/2026, 10:51:50 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i   
        return nums[len(nums) - 1] + 1  
        