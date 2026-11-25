# Last updated: 11/25/2026, 7:58:12 PM
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in count:
            if count[num]  > len(nums)/2 :
                return num