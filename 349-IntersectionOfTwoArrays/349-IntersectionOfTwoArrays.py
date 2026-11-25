# Last updated: 11/25/2026, 7:57:55 PM
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for num in nums1:
            if num in nums2:
                ans.append(num)
        return list(set(ans))
