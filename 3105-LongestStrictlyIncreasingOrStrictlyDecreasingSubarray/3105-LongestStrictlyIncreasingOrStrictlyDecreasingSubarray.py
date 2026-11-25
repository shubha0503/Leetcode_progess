# Last updated: 11/25/2026, 7:53:50 PM
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        icount = 1
        dcount = 1
        count = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                icount += 1
                dcount = 1
            elif nums[i] > nums[i+1]:
                dcount += 1
                icount = 1
            else:
               icount = 1
               dcount = 1
            count = max(count,icount,dcount)
        return count
        