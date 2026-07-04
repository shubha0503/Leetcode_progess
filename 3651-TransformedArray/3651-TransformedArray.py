# Last updated: 7/4/2026, 10:41:20 AM
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
