# Last updated: 8/15/2026, 8:49:18 PM
1class Solution:
2    def longestSubsequence(self, nums: List[int]) -> int:
3        n = len(nums)
4        xor = cnt0 = 0
5        for x in nums:
6            xor ^= x
7            cnt0 += int(x == 0)
8        if xor:
9            return n
10        if cnt0 == n:
11            return 0
12        return n - 1