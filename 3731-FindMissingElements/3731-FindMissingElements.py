# Last updated: 9/16/2026, 11:50:03 AM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        x = []
        for i in range(len(nums)-1):
            for num in range(nums[i]+1,nums[i+1]):
                x.append(num)
        return x
