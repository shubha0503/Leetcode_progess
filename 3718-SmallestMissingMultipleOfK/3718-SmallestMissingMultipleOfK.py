# Last updated: 9/16/2026, 11:50:06 AM
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        for i in count(1):
            x = k * i
            if x not in s:
                return x