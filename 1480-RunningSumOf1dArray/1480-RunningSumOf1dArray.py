# Last updated: 9/16/2026, 11:58:00 AM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            running_sum.append(sum)
        return running_sum
    

