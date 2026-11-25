# Last updated: 11/25/2026, 7:57:04 PM
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = []
        
        for num in nums:
            x = 1
            x = num*num
            ans.append(x)
        ans.sort()
        return ans