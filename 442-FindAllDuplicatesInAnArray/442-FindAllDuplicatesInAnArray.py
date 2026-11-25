# Last updated: 11/25/2026, 7:57:38 PM
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = {}
        sol = []
        for num in nums:
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1
        for num in ans:
            if ans[num] == 2:
                sol.append(num)
        return sol

        