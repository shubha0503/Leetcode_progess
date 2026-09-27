# Last updated: 9/27/2026, 10:28:57 AM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        count = 0
4        max_count = 0
5        for i in range(len(nums)):
6            if nums[i] == 1:
7                count += 1
8            else:
9                count = 0
10            if count > max_count:
11                max_count = count
12        return max_count