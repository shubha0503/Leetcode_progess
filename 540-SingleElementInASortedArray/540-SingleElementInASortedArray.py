# Last updated: 8/2/2026, 11:24:57 AM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        high = len(nums) - 1
        ans = nums[high]
        for i in range(0,high,2):
            if nums[i] != nums[i+1]:
                ans = nums[i]
                break
        return ans
       

        


