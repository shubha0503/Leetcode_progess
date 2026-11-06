# Last updated: 11/6/2026, 10:46:39 PM
1class Solution:
2    def maxSubArray(self, nums: list[int]) -> int:
3        summ = nums[0]
4        current = nums[0]
5        for i in range(1,len(nums)):
6            current = max(current+nums[i],nums[i])
7            summ = max(current,summ)
8        return summ