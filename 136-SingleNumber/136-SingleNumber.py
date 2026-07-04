# Last updated: 7/4/2026, 10:44:43 AM
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result