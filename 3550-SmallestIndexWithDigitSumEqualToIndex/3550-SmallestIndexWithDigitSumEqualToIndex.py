# Last updated: 11/25/2026, 7:52:50 PM
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            s = 0
            while x:
                s += x % 10
                x //= 10
            if s == i:
                return i
        return -1