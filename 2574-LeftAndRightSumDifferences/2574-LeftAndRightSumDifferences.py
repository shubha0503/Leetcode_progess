# Last updated: 9/16/2026, 11:54:58 AM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l, r = 0, sum(nums)
        ans = []
        for x in nums:
            r -= x
            ans.append(abs(l - r))
            l += x
        return ans