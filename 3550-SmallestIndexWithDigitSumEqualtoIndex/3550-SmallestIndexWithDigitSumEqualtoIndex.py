# Last updated: 10/1/2026, 7:17:39 PM
1class Solution:
2    def smallestIndex(self, nums: List[int]) -> int:
3        for i, x in enumerate(nums):
4            s = 0
5            while x:
6                s += x % 10
7                x //= 10
8            if s == i:
9                return i
10        return -1