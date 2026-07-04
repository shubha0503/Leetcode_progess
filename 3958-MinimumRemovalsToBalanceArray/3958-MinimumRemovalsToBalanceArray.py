# Last updated: 7/4/2026, 10:40:54 AM
class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)

        max_keep = 0
        j = 0

        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            max_keep = max(max_keep, j - i)

        return n - max_keep
