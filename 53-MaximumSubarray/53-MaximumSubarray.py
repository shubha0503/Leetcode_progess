# Last updated: 11/6/2026, 10:40:05 PM
1class Solution:
2    def maxSubArray(self, nums: list[int]) -> int:
3        summ = nums[0]
4        current = nums[0]
5    
6        for i in range(1,len(nums)):
7            current = max(current + nums[i], nums[i])
8            summ = max(current,summ)
9        return summ
10            
11