# Last updated: 9/5/2026, 1:08:55 PM
1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        right = [nums[-1]] * n
5        for i in range(n - 2, -1, -1):
6            right[i] = min(right[i + 1], nums[i])
7        left = 0
8        for i, x in enumerate(nums):
9            left = max(left, x)
10            if left - right[i] <= k:
11                return i
12        return -1