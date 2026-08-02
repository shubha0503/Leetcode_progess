# Last updated: 8/2/2026, 11:26:03 AM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = 0
        while low < high :
            mid = (low + high)//2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low 
