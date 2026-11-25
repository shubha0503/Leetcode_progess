# Last updated: 11/25/2026, 7:58:31 PM
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 1:
            return 1
        ans = {}
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                if nums[i] in ans:
                    ans[nums[i + 1]] = ans[nums[i]] + 1
                else:
                    ans[nums[i]] = 1
                    ans[nums[i + 1]] = 2
            else:
                if nums[i] not in ans:
                    ans[nums[i]] = 1
        return max(ans.values())