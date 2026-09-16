# Last updated: 9/16/2026, 11:58:45 AM
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        
        while low <= high:
            mid = (low + high)//2
            result = 0
            for i in range(len(nums)):
                result += ceil(nums[i]/mid)
            if result > threshold:
                low = mid + 1
            else:
                high = mid - 1
        return low

        