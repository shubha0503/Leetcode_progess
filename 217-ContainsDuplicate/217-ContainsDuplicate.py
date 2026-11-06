# Last updated: 11/6/2026, 10:38:00 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set(nums)
4        if len(seen) == len(nums):
5            return False
6        else:
7            return True