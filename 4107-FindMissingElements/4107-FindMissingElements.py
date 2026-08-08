# Last updated: 8/8/2026, 10:47:46 AM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        x = []
        for i in range(len(nums)-1):
            for num in range(nums[i]+1,nums[i+1]):
                x.append(num)
        return x
