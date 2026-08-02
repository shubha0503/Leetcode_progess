# Last updated: 8/2/2026, 11:25:29 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        slow = 0
        for fast in range(n):
            if nums[fast] != 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1

        