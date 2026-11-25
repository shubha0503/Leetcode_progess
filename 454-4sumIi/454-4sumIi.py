# Last updated: 11/25/2026, 7:57:36 PM
class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        ans = 0
        count = {}
        for i in range(len(nums1)):
             for j in range(len(nums2)):
                total = nums1[i] + nums2[j]
                count[total] = count.get(total,0)+1             
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                total = nums3[k] +nums4[l]
                if -total in count:
                    ans += count[-total]
        return ans      


        