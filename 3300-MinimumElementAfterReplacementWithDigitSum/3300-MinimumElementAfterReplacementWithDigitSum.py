# Last updated: 9/16/2026, 11:52:58 AM
class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(b) for b in str(x)) for x in nums)