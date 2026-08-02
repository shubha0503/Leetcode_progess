# Last updated: 8/2/2026, 11:20:04 AM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            running_sum.append(sum)
        return running_sum