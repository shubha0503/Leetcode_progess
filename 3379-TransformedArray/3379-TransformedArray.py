# Last updated: 9/16/2026, 11:52:47 AM
class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        ans = []

        for i in range(n):
            if nums[i] == 0:
                ans.append(0)
            else:
                idx = (i + nums[i]) % n
                ans.append(nums[idx])

        return ans
